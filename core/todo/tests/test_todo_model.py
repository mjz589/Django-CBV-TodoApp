from django.test import TestCase
from ..models import Task
from accounts.models import User, Profile


class TestTaskModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='test!1234')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'test_first',
            last_name = 'test_last',
            description = 'this is a test',
        )

    def test_create_task_object_with_valid_data(self):
        task = Task.objects.create(
            user = self.profile,
            title = 'test',
            complete = True,
        )
        self.assertTrue(Task.objects.filter(pk = task.id).exists())
        self.assertEqual(task.title, 'test')