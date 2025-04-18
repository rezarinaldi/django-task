from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='index'),
    path('<int:id>', views.NoteDetailView.as_view(), name='note'),
    path('create/', views.NoteCreateView.as_view(), name='note_create'),
]