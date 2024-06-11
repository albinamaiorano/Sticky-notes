from django import forms  # Importing forms module from Django
from .models import Note, Post  # Importing Note and Post models from the current package


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note instances.
    Inherits from Django's ModelForm.
    """

    class Meta:
        """
        Meta class for NoteForm.
        """

        model = Note  # Specifies the model to be used for this form
        fields = ['title', 'content']  # Specifies the fields to include in the form


class PostForm(forms.ModelForm):
    """
    Form for creating and updating Post instances.
    Inherits from Django's ModelForm.
    """

    class Meta:
        """
        Meta class for PostForm.
        """

        model = Post  # Specifies the model to be used for this form
        fields = ['title', 'content']  # Specifies the fields to include in the form
