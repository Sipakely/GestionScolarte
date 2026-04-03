from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_note, name='ajouter_note'),
    path('bulletin/<int:etudiant_id>/', views.bulletin, name='bulletin'),
]