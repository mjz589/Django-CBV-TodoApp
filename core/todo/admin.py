from django.contrib import admin
from .models import *
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'user', 'complete', 'created_date',)
    list_filter = ('complete', ) 
    #ordering = ('-created_date',)
    search_fields = ('title', 'user',)

admin.site.register(Task, TaskAdmin)