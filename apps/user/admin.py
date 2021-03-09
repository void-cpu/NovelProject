from django.contrib import admin

from .models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAnotherConfig)
class UserAnother(admin.ModelAdmin):
    pass
