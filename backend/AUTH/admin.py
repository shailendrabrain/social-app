from django.contrib import admin
from .models import AuthUser


@admin.register(AuthUser)
class User(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
