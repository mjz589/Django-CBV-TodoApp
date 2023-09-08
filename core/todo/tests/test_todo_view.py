from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from ..models import Task


class TestTodoView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test1@test.com', password='test/!1234')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'test_first',
            last_name = 'test_last',
            description = 'this is a test',
        )
        self.task = Task.objects.create(
            user = self.profile,
            title = 'test1',
            complete = False,
        )

    def test_todo_task_list_anonymouse_response(self):
        url = reverse('todo:task_list') 
        response = self.client.get(url)
        # http response 302 for it redirects to login page
        self.assertEquals(response.status_code, 302) 
        self.assertTrue(str(response.content).find('task_list'))
        
    def test_todo_task_list_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('todo:task_list')
        response = self.client.get(url, follow=True)
        
        self.assertRedirects(response, '/accounts/login/?next=/')
        self.assertEqual(response.status_code, 200)
            
        # self.assertTemplateUsed(response, template_name = "todo/task_list.html")