from django.test import SimpleTestCase, TestCase

from ..forms import CreateTaskForm, UpdateTaskForm


class TestTaskFrom(SimpleTestCase):

    def test_create_task_from_with_valid_data(self):
        form = CreateTaskForm(data={'title': 'test'})
        self.assertTrue(form.is_valid())

    def test_update_task_from_with_valid_data(self):
        form = UpdateTaskForm(data={'title': 'test'})
        self.assertTrue(form.is_valid())