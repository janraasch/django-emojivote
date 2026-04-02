from django.contrib import admin

from .models import Emoji


@admin.register(Emoji)
class EmojiAdmin(admin.ModelAdmin):
    list_display = ("character", "name", "votes", "created_at")
