from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name  = 'accounts'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),

    # email test
    path('test-email/', views.EmailTestSend.as_view(), name='test-email'),
    # activation
    path('activation/confirm/<str:token>', views.ActivationApiView.as_view(), name='activation'),
    # resend activation
    path('activation/resend/', views.ActivationResendApiView.as_view(), name='activation-resend'),
    
    # change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),

    # reset password
    path('reset-password/', views.ResetPasswordApiView.as_view(), name='reset-password'),
    # login/logout token
    path('token/login/', views.CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    # login jwt
    path('jwt/create/', views.CostumTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    #profile
    path('profile/', views.ProfileApiView.as_view(), name='profile'),
]
