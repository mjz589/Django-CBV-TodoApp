import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User, Profile
from todo.models import Task


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="test333@test.com", password="test/!1234", is_verified=True
    )
    return user


@pytest.fixture
def create_task(common_user):
    user = Profile.objects.get(user=common_user)
    task = Task.objects.create(
        user=user,
        title="test",
        complete=False,
    )
    return task


@pytest.mark.django_db
class TestTaskModels:
    def test_get_task_list_response_302_status(self, api_client):
        # without authentication and redirect to login url
        url = reverse("todo:task_list")
        response = api_client.get(url)
        assert response.status_code == 302

    def test_get_task_list_response_200_status(
        self, api_client, common_user, create_task
    ):
        # show task list after redirecting to login url for authenticatication
        url = reverse("todo:task_list")
        task = create_task
        user = common_user
        api_client.force_authenticate(user)
        response = api_client.get(url, follow=True)
        assert response.status_code == 200
        assert Task.objects.filter(user=task.user, title=task.title).exists()

    def test_post_task_create_response_200_status(self, api_client, common_user):
        # craete a task after redirecting to login url for authenticatication
        user = common_user
        url = reverse("todo:task_list")
        api_client.force_authenticate(user)
        data = {
            "user": user,
            "title": "TestTask-created",
            "complete": True,
        }
        response = api_client.post(url, data=data, follow=True)
        assert response.status_code == 200

    def test_patch_task_complete_response_200_status(
        self, api_client, common_user, create_task
    ):
        # make a task complete true value after redirecting to login url for authenticatication
        user = common_user
        url = reverse("todo:complete_task", kwargs={"pk": create_task.id})
        api_client.force_authenticate(user)
        data = {
            "complete": True,
        }
        response = api_client.patch(url, data=data, follow=True)
        assert response.status_code == 200

    def test_patch_task_rename_response_200_status(
        self, api_client, common_user, create_task
    ):
        # make a task complete true value after redirecting to login url for authenticatication
        user = common_user
        url = reverse("todo:complete_task", kwargs={"pk": create_task.id})
        api_client.force_authenticate(user)
        data = {
            "title": "Task renamed",
        }
        response = api_client.patch(url, data=data, follow=True)
        assert response.status_code == 200

    def test_delete_task_response_200_status(
        self, api_client, common_user, create_task
    ):
        # delete a task after redirecting to login url for authenticatication
        user = common_user
        url = reverse("todo:delete_task", kwargs={"pk": create_task.id})
        api_client.force_authenticate(user)
        response = api_client.delete(url, follow=True)
        assert response.status_code == 200
