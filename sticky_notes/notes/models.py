from django.db import models


class Note(models.Model):
    """Model representing a note."""
    title = models.CharField(max_length=100, help_text="Enter the title of the note.")
    content = models.TextField(help_text="Enter the content of the note.")

    def __str__(self):
        """String for representing the Note object."""
        return self.title
