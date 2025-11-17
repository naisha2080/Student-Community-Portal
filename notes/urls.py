from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_home_view, name = 'notes_home'),
    path('<int:pk>/delete/', views.notes_delete_view, name='note_delete'),
]