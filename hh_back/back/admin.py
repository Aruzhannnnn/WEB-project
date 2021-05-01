from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from back.models import About, Tour, Comment

admin.site.register(About)

admin.site.register(Tour)
admin.site.register(Comment)
