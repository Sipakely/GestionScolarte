from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
]    path('', views.liste_etudiants, name='liste_etudiants'),
