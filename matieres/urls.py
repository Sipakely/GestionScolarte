from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_matieres, name='liste_matieres'),
    path('ajouter/', views.ajouter_matiere, name='ajouter_matiere'),
    path('modifier/<int:id>/', views.modifier_matiere, name='modifier_matiere'),
    path('supprimer/<int:id>/', views.supprimer_matiere, name='supprimer_matiere'),
]