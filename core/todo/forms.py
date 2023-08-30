from django import forms
from .models import *

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)

class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    
    class Meta:
        model = Task
        fields = ('title',)
