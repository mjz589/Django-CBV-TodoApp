from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task 
# or instead of ...models you can point models.py like this: todo.models
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def taskList(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def taskDetail(request,id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response({'detail':'item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
