from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
# from taggit.managers import TaggableManager
# from ckeditor_uploader.fields import RichTextUploadingField 
# from django.core.exceptions import ValidationError
# from blog.formatChecker import ContentTypeRestrictedFileField


# from accounts.models import Profile
# from django.contrib.auth import get_user_model
# --- getting user model object ---
# User = get_user_model()


# Create your models here.

# user comes from accounts.Profile
class Task(models.Model):
    user = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = "user"
        
