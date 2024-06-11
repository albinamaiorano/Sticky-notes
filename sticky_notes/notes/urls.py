from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the root URL, linking to the home view

    # URLs for Notes
    path('notes/', views.note_list, name='note_list'),  # URL pattern to list all notes
    path('note/<int:pk>/', views.note_detail, name='note_detail'),  # URL pattern for the detail view of a specific note
    path('note/new/', views.note_create, name='note_create'),  # URL pattern to create a new note
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),  # URL pattern to edit an existing note
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),  # URL pattern to delete a specific note

    # URLs for Posts
    path('posts/', views.post_list, name='post_list'),  # URL pattern to list all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL pattern for the detail view of a specific post
    path('post/new/', views.post_new, name='post_new'),  # URL pattern to create a new post
]

