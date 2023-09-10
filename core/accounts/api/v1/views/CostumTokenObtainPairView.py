from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from ..serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# custom TokenObtainPairView
class CostumTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [
        IsAuthenticated,
    ]
