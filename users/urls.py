from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('', views.liste_etudiants, name='liste_etudiants'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    ]