# Author: Andile Gumede
# Date:   2025-11-20

"""Data models for the Notes app.

Defines the database schema for sticky notes, including their
title, content, colour label, and timestamps.
"""

from django.db import models


class Note(models.Model):
    """A single sticky note with a title, content, colour, and timestamps.

    Attributes:
        COLOUR_CHOICES (list): Valid colour options available for a note.
        title (CharField): Short heading of the note, max 255 characters.
        content (TextField): Main body text of the note.
        colour (CharField): Background colour label, defaults to 'yellow'.
        created_at (DateTimeField): Timestamp set automatically on creation.
        updated_at (DateTimeField): Timestamp updated automatically on save.
    """

    COLOUR_CHOICES = [
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    colour = models.CharField(
        max_length=10,
        choices=COLOUR_CHOICES,
        default='yellow',
    )

    # Set once at creation; never modified on subsequent saves.
    created_at = models.DateTimeField(auto_now_add=True)

    # Refreshed automatically every time the instance is saved.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for the Note model."""

        # Display most recently edited notes first in querysets.
        ordering = ['-updated_at']

    def __str__(self) -> str:
        """Return the note title as its string representation.

        Returns:
            str: The title of the note.
        """
        return self.title
