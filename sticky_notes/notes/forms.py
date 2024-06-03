from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating Note instances."""

    class Meta:
        model = Note  # Specify the model to use
        fields = ['title', 'content']  # Specify the fields to include in the form
