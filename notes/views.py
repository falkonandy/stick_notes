# Author: Andile Gumede
# Date:   2026-11-19

"""View functions for the Notes app.

Handles the HTTP request/response cycle for creating, listing,
viewing, updating, and deleting sticky notes.
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """Display a list of all sticky notes.

    Args:
        request (HttpRequest): The incoming HTTP GET request.

    Returns:
        HttpResponse: Rendered ``notes/note_list.html`` template with
            all notes and a page title.
    """
    notes = Note.objects.all()
    return render(
        request,
        "notes/note_list.html",
        {
            "notes": notes,
            "page_title": "My Sticky Notes",
        },
    )


def note_detail(request, pk):
    """Display a single sticky note.

    Args:
        request (HttpRequest): The incoming HTTP GET request.
        pk (int): Primary key of the note to retrieve.

    Returns:
        HttpResponse: Rendered ``notes/note_detail.html`` template with
            the requested note.

    Raises:
        Http404: If no note with the given ``pk`` exists.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Create a new sticky note.

    Renders a blank form on GET. Validates and saves the note on POST,
    then redirects to the note list on success.

    Args:
        request (HttpRequest): The incoming HTTP GET or POST request.

    Returns:
        HttpResponse: Rendered ``notes/note_form.html`` template with
            the form on GET or invalid POST, or a redirect to
            ``note_list`` on successful save.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "action": "Create",
            "page_title": "New Note",
        },
    )


def note_update(request, pk):
    """Update an existing sticky note.

    Renders a pre-populated form on GET. Validates and saves changes on
    POST, then redirects to the note list on success.

    Args:
        request (HttpRequest): The incoming HTTP GET or POST request.
        pk (int): Primary key of the note to update.

    Returns:
        HttpResponse: Rendered ``notes/note_form.html`` template with
            the populated form on GET or invalid POST, or a redirect to
            ``note_list`` on successful save.

    Raises:
        Http404: If no note with the given ``pk`` exists.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "action": "Update",
            "page_title": f"Edit: {note.title}",
        },
    )


def note_delete(request, pk):
    """Delete a sticky note after confirmation.

    Renders a confirmation page on GET. Deletes the note on POST and
    redirects to the note list.

    Args:
        request (HttpRequest): The incoming HTTP GET or POST request.
        pk (int): Primary key of the note to delete.

    Returns:
        HttpResponse: Rendered ``notes/note_confirm_delete.html``
            template on GET, or a redirect to ``note_list`` after
            deletion on POST.

    Raises:
        Http404: If no note with the given ``pk`` exists.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
