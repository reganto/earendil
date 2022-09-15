import os

from celery import Celery


DJANGO_ENV = os.environ.get("DJANGO_ENV", "local")
SETTING_PATH = f"config.settings.{DJANGO_ENV}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTING_PATH)
app = Celery("celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
