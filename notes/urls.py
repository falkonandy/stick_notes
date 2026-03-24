"""URL configuration for the Notes app.

Defines the URL patterns that map HTTP routes to their corresponding
view functions for creating, reading, updating, and deleting notes.

URL Patterns:
    /: Lists all notes.
    /notes/<pk>/: Retrieves a single note by primary key.
    /notes/create/: Creates a new note.
    /notes/<pk>/edit/: Updates an existing note by primary key.
    /notes/<pk>/delete/: Deletes a note by primary key.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("notes/<int:pk>/", views.note_detail, name="note_detail"),
    path("notes/create/", views.note_create, name="note_create"),
    path("notes/<int:pk>/edit/", views.note_update, name="note_update"),
    path("notes/<int:pk>/delete/", views.note_delete, name="note_delete"),
]
