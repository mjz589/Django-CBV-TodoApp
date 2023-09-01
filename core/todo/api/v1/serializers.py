from rest_framework import serializers
from ...models import Task

# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     complete = serializers.BooleanField()

class TaskSerializer(serializers.ModelSerializer):
    # user must automatically be provided and not be written by users
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'complete',)