# Author: Andile Gumede
# Date:   2025-11-22

"""Unit and integration tests for the Notes app.

Covers model integrity, form validation, and all five CRUD views
using Django's built-in test client.
"""

from django.test import TestCase, Client
from django.urls import reverse

from .models import Note
from .forms import NoteForm


# ---------------------------------------------------------------------------
# Model Tests
# ---------------------------------------------------------------------------


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def setUp(self):
        """Create a shared Note instance for model tests."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is test content.",
            colour="yellow",
        )

    def test_note_creation(self):
        """Note is saved correctly with expected field values."""
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is test content.")
        self.assertEqual(self.note.colour, "yellow")

    def test_str_returns_title(self):
        """__str__ returns the note title."""
        self.assertEqual(str(self.note), "Test Note")

    def test_default_colour_is_yellow(self):
        """Colour field defaults to 'yellow' when not specified."""
        note = Note.objects.create(title="No Colour", content="...")
        self.assertEqual(note.colour, "yellow")

    def test_created_at_is_set_on_creation(self):
        """created_at is populated automatically on save."""

        self.assertIsNotNone(self.note.created_at)

    def test_updated_at_changes_on_save(self):
        """updated_at is refreshed every time the note is saved."""

        original_updated_at = self.note.updated_at
        self.note.title = "Updated Title"
        self.note.save()
        self.note.refresh_from_db()
        self.assertGreaterEqual(self.note.updated_at, original_updated_at)

    def test_ordering_is_most_recently_updated_first(self):
        """Queryset default ordering returns most recently
        edited notes first."""

        older = Note.objects.create(title="Older", content="...")
        newer = Note.objects.create(title="Newer", content="...")
        notes = list(Note.objects.all())
        self.assertEqual(notes[0], newer)
        self.assertEqual(notes[1], older)


# Form Tests


class NoteFormTest(TestCase):
    """Tests for the NoteForm ModelForm."""

    def test_valid_form(self):
        """Form is valid when all required fields are provided."""
        form = NoteForm(
            data={
                "title": "Valid Title",
                "content": "Valid content.",
                "colour": "blue",
            }
        )
        self.assertTrue(form.is_valid())

    def test_missing_title_is_invalid(self):
        """Form is invalid when title is missing."""
        form = NoteForm(
            data={
                "title": "",
                "content": "Some content.",
                "colour": "green",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_missing_content_is_invalid(self):
        """Form is invalid when content is missing."""
        form = NoteForm(
            data={
                "title": "A Title",
                "content": "",
                "colour": "pink",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)

    def test_invalid_colour_choice_is_rejected(self):
        """Form is invalid when an unrecognised colour is submitted."""
        form = NoteForm(
            data={
                "title": "A Title",
                "content": "Some content.",
                "colour": "orange",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("colour", form.errors)


# ---------------------------------------------------------------------------
# View Tests
# ---------------------------------------------------------------------------


class NoteViewTest(TestCase):
    """Integration tests for all five Note CRUD views."""

    def setUp(self):
        """Set up a test client and a shared Note instance."""
        self.client = Client()
        self.note = Note.objects.create(
            title="View Test Note",
            content="Content for view tests.",
            colour="purple",
        )

    # --- note_list ---

    def test_note_list_returns_200(self):
        """GET note_list returns HTTP 200."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)

    def test_note_list_uses_correct_template(self):
        """note_list renders notes/note_list.html."""
        response = self.client.get(reverse("note_list"))
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_list_contains_note(self):
        """note_list response includes the existing note title."""
        response = self.client.get(reverse("note_list"))
        self.assertContains(response, "View Test Note")

    # --- note_detail ---

    def test_note_detail_returns_200(self):
        """GET note_detail returns HTTP 200 for a valid pk."""
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_returns_404_for_missing_note(self):
        """GET note_detail returns HTTP 404 for a non-existent pk."""
        response = self.client.get(reverse("note_detail", args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_note_detail_uses_correct_template(self):
        """note_detail renders notes/note_detail.html."""
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertTemplateUsed(response, "notes/note_detail.html")

    # --- note_create ---

    def test_note_create_get_returns_200(self):
        """GET note_create returns HTTP 200 with a blank form."""
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)

    def test_note_create_post_creates_note_and_redirects(self):
        """Valid POST to note_create saves a new note and redirects."""
        count_before = Note.objects.count()
        response = self.client.post(
            reverse("note_create"),
            data={
                "title": "Brand New Note",
                "content": "Fresh content.",
                "colour": "green",
            },
        )
        self.assertEqual(Note.objects.count(), count_before + 1)
        self.assertRedirects(response, reverse("note_list"))

    def test_note_create_invalid_post_returns_form(self):
        """Invalid POST to note_create re-renders the form without saving."""
        count_before = Note.objects.count()
        response = self.client.post(
            reverse("note_create"),
            data={
                "title": "",
                "content": "",
                "colour": "yellow",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), count_before)

    # --- note_update ---

    def test_note_update_get_returns_200(self):
        """GET note_update returns HTTP 200 with a pre-populated form."""
        response = self.client.get(reverse("note_update", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_update_post_saves_changes_and_redirects(self):
        """Valid POST to note_update persists changes and redirects."""
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            data={
                "title": "Updated Title",
                "content": "Updated content.",
                "colour": "blue",
            },
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")
        self.assertRedirects(response, reverse("note_list"))

    def test_note_update_returns_404_for_missing_note(self):
        """GET note_update returns HTTP 404 for a non-existent pk."""
        response = self.client.get(reverse("note_update", args=[9999]))
        self.assertEqual(response.status_code, 404)

    # --- note_delete ---

    def test_note_delete_get_returns_200(self):
        """GET note_delete returns HTTP 200 with a confirmation page."""
        response = self.client.get(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_note_delete_post_deletes_note_and_redirects(self):
        """POST to note_delete removes the note and redirects."""
        response = self.client.post(
            reverse("note_delete", args=[self.note.pk]))
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
        self.assertRedirects(response, reverse("note_list"))

    def test_note_delete_returns_404_for_missing_note(self):
        """GET note_delete returns HTTP 404 for a non-existent pk."""
        response = self.client.get(reverse("note_delete", args=[9999]))
        self.assertEqual(response.status_code, 404)
