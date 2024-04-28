from django.contrib import admin
from django.contrib.admin import ModelAdmin

from note.models import Category, Note


@admin.register(Note)
class NoteAdmin(ModelAdmin):
    list_display = ("id", "status", "created_at", "category")
    list_filter = ("status", "category", "created_at")
    ordering = ("created_at", )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("category")


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "name", "color")
    list_filter = ("color", )
    ordering = ("name", )