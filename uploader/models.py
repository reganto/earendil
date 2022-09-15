from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Video(models.Model):
    title = models.CharField(
        max_length=1024, verbose_name=_("Title"), help_text=_("Title of uploaded video")
    )
    original = models.FileField(
        upload_to="media/videos/",
        verbose_name=_("Original"),
        help_text=_("Original quality of uploaded video"),
    )
    video_240 = models.FileField(
        upload_to="media/240/",
        null=True,
        blank=True,
        verbose_name=_("240_quality"),
        help_text=_("240 video quality"),
    )
    video_360 = models.FileField(
        upload_to="media/360/",
        null=True,
        blank=True,
        verbose_name=_("360_quality"),
        help_text=_("360 video quality"),
    )
    elapsed_time = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Elapsed Time"),
        help_text=_("Elapsed time for video quality conversion"),
    )

    def __str__(self):
        return f"{self.title}"
