from celery import shared_task

from .models import Task


@shared_task
def delete_completed_tasks():
    return Task.objects.filter(complete=True).delete()
