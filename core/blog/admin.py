from django.contrib import admin
from .models import *
# Register your models here.


# @admin.register(Post)       # alterative way of registering
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('title', 'author', 'status', 'created_date', 'published_date') #'login_require',
    list_filter = ('status', 'author', 'category') #,'login_require'
    #ordering = ('-created_date',)
    search_fields = ['title', 'content']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)