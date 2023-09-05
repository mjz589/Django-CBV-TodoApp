from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
# email
# from django.core.mail import send_mail
# from mail_templated import send_mail
from mail_templated import EmailMessage
from ...utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


# email
class EmailTestSend(generics.GenericAPIView):
    # def get(self, *args, **kwargs):
    #     self.email = 'mjz589.2018@gmail.com'
    #     user_obj = get_object_or_404(User, email=self.email)
    #     token = self.get_tokens_for_user(user_obj)
    #     email_obj = EmailMessage(
    #         'email/activation_email.tpl',
    #         {'token': token },
    #         'admin@admin.com',
    #         to=[self.email]
    #     )
    #     EmailThread(email_obj).start()
    #     return Response('email sent')
    
    # # get access token for user
    # def get_tokens_for_user(self, user):
    #     refresh = RefreshToken.for_user(user)
    #     return str(refresh.access_token)
    pass
