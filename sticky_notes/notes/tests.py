import os  # Import the os module for operating system functionality
import django  # Import the Django module for Django framework functionalities
import sys  # Import the sys module for system-specific functionalities

# Add the project directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')
django.setup()

from django.test import TestCase, Client  # Import necessary modules for testing
from django.urls import reverse  # Import the reverse function to generate URLs
from notes.models import Note, Post  # Import models from the notes app
from notes.forms import NoteForm, PostForm  # Import forms from the notes app

class NoteModelTests(TestCase):
    def setUp(self):
        """Set up a test note instance."""
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_creation(self):
        """Test the creation of a note."""
        self.assertEqual(self.note.title, 'Test Note')  # Check if the title matches
        self.assertEqual(self.note.content, 'This is a test note.')  # Check if the content matches

class PostModelTests(TestCase):
    def setUp(self):
        """Set up a test post instance."""
        self.post = Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_creation(self):
        """Test the creation of a post."""
        self.assertEqual(self.post.title, 'Test Post')  # Check if the title matches
        self.assertEqual(self.post.content, 'This is a test post.')  # Check if the content matches

class NoteViewsTests(TestCase):
    def setUp(self):
        """Set up the test client and a test note instance."""
        self.client = Client()  # Create a test client
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        """Test the note list view."""
        response = self.client.get(reverse('note_list'))  # Send a GET request to the note list view
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, self.note.title)  # Check if the note title is present in the response

    def test_note_detail_view(self):
        """Test the note detail view."""
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))  # Send a GET request to the note detail view
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, self.note.title)  # Check if the note title is present in the response

class PostViewsTests(TestCase):
    def setUp(self):
        """Set up the test client and a test post instance."""
        self.client = Client()  # Create a test client
        self.post = Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_list_view(self):
        """Test the post list view."""
        response = self.client.get(reverse('post_list'))  # Send a GET request to the post list view
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, self.post.title)  # Check if the post title is present in the response

    def test_post_detail_view(self):
        """Test the post detail view."""
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))  # Send a GET request to the post detail view
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, self.post.title)  # Check if the post title is present in the response

class NoteFormTests(TestCase):
    def test_valid_note_form(self):
        """Test the validation of a valid note form."""
        form_data = {'title': 'Test Note', 'content': 'This is a test note.'}  # Define valid form data
        form = NoteForm(data=form_data)  # Create a form instance with the valid data
        self.assertTrue(form.is_valid())  # Check if the form is valid

    def test_invalid_note_form(self):
        """Test the validation of an invalid note form."""
        form_data = {'title': '', 'content': ''}  # Define invalid form data
        form = NoteForm(data=form_data)  # Create a form inst
