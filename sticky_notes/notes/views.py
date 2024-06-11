from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Post
from .forms import NoteForm, PostForm

# Home view
def home(request):
    """
    View for the home page.
    """
    return render(request, 'notes/home.html')

# Post views

def post_list(request):
    """
    View to list all posts.
    """
    posts = Post.objects.all()
    return render(request, 'notes/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """
    View to show details of a single post.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'notes/post_detail.html', {'post': post})

def post_new(request):
    """
    View to create a new post.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'notes/post_edit.html', {'form': form})

# Note views

def note_list(request):
    """
    View to list all notes.
    """
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    """
    View to show details of a single note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    """
    View to create a new note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_update(request, pk):
    """
    View to update an existing note.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    """
    View to delete a note.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
