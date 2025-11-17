from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements_home_view, name = 'announcements_home'),
]