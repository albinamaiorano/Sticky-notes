from django.test import TestCase, Client
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteModelTests(TestCase):
    """Test cases for the Note model."""

    def setUp(self):
        """Set up a Note instance for testing."""
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_creation(self):
        """Test that a Note instance is created correctly."""
        self.assertEqual(self.note.title, 'Test Note')
        self.assertEqual(self.note.content, 'This is a test note.')


class NoteViewsTests(TestCase):
    """Test cases for the views related to Note."""

    def setUp(self):
        """Set up the test client and a Note instance for testing."""
        self.client = Client()
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        """Test the note_list view."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_note_detail_view(self):
        """Test the note_detail view."""
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)


class NoteFormTests(TestCase):
    """Test cases for the NoteForm."""

    def test_valid_form(self):
        """Test a valid NoteForm."""
        form_data = {'title': 'Test Note', 'content': 'This is a test note.'}
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test an invalid NoteForm."""
        form_data = {'title': '', 'content': ''}
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())
