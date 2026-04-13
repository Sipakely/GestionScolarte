from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('ajouter/', views.ajouter_etudiant, name='ajouter'),
    path('', views.liste_etudiants, name='liste'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    ]