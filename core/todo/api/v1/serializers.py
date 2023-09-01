from rest_framework import serializers
from ...models import Task

# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     complete = serializers.BooleanField()

class TaskSerializer(serializers.ModelSerializer):
    # user must automatically be provided and not be written by users
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'complete', 'relative_url', 'absolute_url', 'created_date')

    