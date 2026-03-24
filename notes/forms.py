# Author: Andile Gumede
# Date:   2025-11-20

"""Forms for the Notes app.

Defines the ModelForm used to create and edit sticky notes,
including widget configuration for styling.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """ModelForm for creating and editing a sticky note.

    Renders form fields for 'title', 'content', and 'colour',
    each with custom HTML attributes for frontend styling.

    Attributes:
        Meta.model (Note): The model this form is bound to.
        Meta.fields (list): Fields exposed in the form.
        Meta.widgets (dict): Custom widget configuration per field.
    """

    class Meta:
        """Configures the model, fields, and widgets for 'NoteForm'."""

        model = Note
        fields = ["title", "content", "colour"]
        widgets = {
            # Single-line text input with autofocus.
            "title": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Note title…",
                    "autofocus": True,
                }
            ),
            # Multi-line textareag.
            "content": forms.Textarea(
                attrs={
                    "class": "form-textarea",
                    "placeholder": "Write your note here…",
                    "rows": 7,
                }
            ),
            # Dropdown select.
            "colour": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
