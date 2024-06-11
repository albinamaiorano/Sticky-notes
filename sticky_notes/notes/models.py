from django.db import models


class Note(models.Model):
    """
    A model representing a note with a title, content, and a creation timestamp.
    """
    title = models.CharField(max_length=200)  # Title of the note
    content = models.TextField()  # Content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the note was created

    def __str__(self):
        """
        Returns the string representation of the Note object,
        which is the title of the note.
        """
        return self.title


class Post(models.Model):
    """
    A model representing a post with a title, content, and a creation timestamp.
    """
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the post was created

    def __str__(self):
        """
        Returns the string representation of the Post object,
        which is the title of the post.
        """
        return self.title
