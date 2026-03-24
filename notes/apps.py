# Author: Andile Gumede
# Date:   2025-11-21

"""App configuration for the Notes app.

Registers the Notes application with Django's and defines
app-level settings such as the default primary key type.
"""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Django app configuration for the Notes app.

    Attributes:
        default_auto_field (str): Specifies BigAutoField as the default
            primary key type for all models in this app.
        name (str): The dotted Python path used to identify this app
            within the Django project.
    """

    # Use 64-bit integer primary keys for all models by default.
    default_auto_field = "django.db.models.BigAutoField"

    # Must match the app's directory name and INSTALLED_APPS entry.
    name = "notes"
