from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_matieres, name='liste_matieres'),
    path('ajouter/', views.ajouter_matiere, name='ajouter_matiere'),
]