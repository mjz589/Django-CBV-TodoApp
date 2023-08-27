from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    """
    it already exists even without writing it. because UserAdmin has this.
    """
    class Meta:
        model = User
        fields = ('email',)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm # it already exists even without writing it. because UserAdmin has this.

    model = User
    list_display = ('email', 'is_superuser', 'is_active',)
    list_filter = ('email', 'is_superuser', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active','is_superuser',
            ),
        }),
        ('Group Permissions', {
            "fields": (
                'groups', 'user_permissions',
            ),
        }),
        ('Important Date', {
            "fields": (
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        ('None', {
            "classes": ('wide',),
            "fields": (
                'email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser',
            ),
        }),

    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
