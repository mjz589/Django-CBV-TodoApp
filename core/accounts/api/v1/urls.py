from django.urls import path, include
from . import views


app_name  = 'accounts'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration')

    # change password
    # reset password
    # login token
    # login jwt
]
