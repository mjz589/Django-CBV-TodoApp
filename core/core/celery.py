import os

from celery import Celery
from celery.schedules import crontab
from todo.tasks import delete_completed_tasks

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.conf.timezone = "Asia/Tehran"
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 minutes.
    sender.add_periodic_task(
        crontab(
            minute="*/10",
        ),
        delete_completed_tasks.s(),
        name="delete completed tasks",
    )
