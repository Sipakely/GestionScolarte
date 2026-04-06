from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_notes, name='liste_notes'),
    path('ajouter/', views.ajouter_note, name='ajouter_note'),
]