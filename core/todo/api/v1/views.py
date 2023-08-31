from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task 
# or instead of ...models you can point models.py like this: todo.models
# from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view()
def taskDetail(request,id):
    task = get_object_or_404(Task, pk=id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

