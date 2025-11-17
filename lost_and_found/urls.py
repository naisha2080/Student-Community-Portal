from django.urls import path
from . import views

urlpatterns = [
    path('', views.lost_found_home_view, name = 'lost_found_home'),
    path('<int:pk>/delete/', views.lost_found_delete_view, name='lost_found_delete'),
    path('<int:pk>/claim/', views.lost_found_claim_view, name='lost_found_claim'),
]