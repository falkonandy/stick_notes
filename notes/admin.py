# Author: Andile Gumede
# Date:   2025-11-21

"""Admin configuration for the Notes app.

Registers the Note model with the Django admin site and customises
the list view with display columns, filters, and search capability.
"""

from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Note model.

    Attributes:
        list_display (tuple): Columns shown in the admin list view.
        list_filter (tuple): Sidebar filters available in the list view.
        search_fields (tuple): Fields searched when using the admin
            search bar.
    """

    # Columns rendered in the changelist table.
    list_display = ("title", "colour", "created_at", "updated_at")

    # Sidebar filter panel — allows narrowing notes by colour.
    list_filter = ("colour",)

    # Enables full-text search across title and content fields.
    search_fields = ("title", "content")
