from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task 
# or instead of ...models you can point models.py like this: todo.models


@api_view()
def taskList(request):
    return Response({"Mohamad Javad": "Mikey"})

@api_view()
def taskDetail(request,id):
    task = Task.objects.get(pk=id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)
