from django.contrib import admin

from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(NovelClass)
class NovelClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    pass


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass
