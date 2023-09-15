from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo"
    # def ready(self):
    #     from .tasks import delete_completed_tasks
    #     delete_completed_tasks.delay()
