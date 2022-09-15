import uuid
import subprocess
from pathlib import Path
from time import perf_counter

from django.core.files import File

from celery import shared_task


@shared_task()
def convert(video_pk):
    """
    Celery task operation to generate 240 and 350 quality of a particular video.
    """
    # TODO: split convert to two smaller task
    # TODO: generate execution time with celery signals
    start = perf_counter()
    from uploader.models import Video

    try:
        _video = Video.objects.get(pk=video_pk)
    except Video.DoesNotExist:
        print("Video Does not exist")
    else:
        name = Path(_video.original.name).stem + str(uuid.uuid1())
        subprocess.call(
            [
                "ffmpeg",
                "-i",
                _video.original.path,
                "-threads",
                "0",
                "-preset",
                "ultrafast",
                "-s",
                "320x240",
                "-c:v",
                "libx264",
                f"/tmp/{name}_240.mp4",
            ]
        )
        subprocess.call(
            [
                "ffmpeg",
                "-i",
                _video.original.path,
                "-threads",
                "0",
                "-preset",
                "ultrafast",
                "-s",
                "640x360",
                "-c:v",
                "libx264",
                f"/tmp/{name}_360.mp4",
            ]
        )
        f1 = File(open(f"/tmp/{name}_240.mp4", "rb"))
        f2 = File(open(f"/tmp/{name}_360.mp4", "rb"))
        _video.video_240.save(name, f1)
        _video.video_360.save(name, f2)
        # TODO: remove temporary videos
        end = perf_counter() - start
        _video.elapsed_time = end
        _video.save()
