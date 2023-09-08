from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile

class TestTodoView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@test.com', password='test!1234')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'test_first',
            last_name = 'test_last',
            description = 'this is a test',
        )
        self.task = Task.objects.create(
            user = self.profile,
            title = 'test',
            complete = True,
        )
    def test_todo_index_url_successful_response(self):
        url = reverse('todo:task_list') 
        response = self.client.get(url)
        # http response 302 for it redirects to login page
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(str(response.content).find('task_list'))
        # self.assertTemplateUsed(response, template_name='todo/task_list.html')