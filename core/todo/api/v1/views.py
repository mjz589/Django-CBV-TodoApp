from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task

# or instead of ...models you can point models.py like this: todo.models
from accounts.models import Profile

# class-based views for api
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

# from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    # filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        "complete",
    ]
    search_fields = [
        "title",
    ]
    ordering_fields = ["created_date"]
    # pagination
    pagination_class = DefaultPagination

    """ --- we used another method for user providing ---
    def perform_create(self, serializer):
        # user must automatically be provided and not be written by users
        profile = Profile.objects.get(user=self.request.user.id)
        serializer.save(user=profile) """

    def get_queryset(self):
        # define the queryset wanted
        if self.request.user.is_verified:
            profile = Profile.objects.get(user=self.request.user.id)
            queryset = Task.objects.filter(user=profile.id)
        else:
            raise serializers.ValidationError({"detail": "User is not verified."})
        return queryset

    # extra actions
    @action(
        methods=[
            "GET",
        ],
        detail=False,
    )
    def get_ok(self, request):
        return Response({"detail": "extra actions -OK-"})
