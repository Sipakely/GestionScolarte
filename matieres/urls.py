from django.urls import path
from . import views

app_name = 'matieres'
urlpatterns = [
    path('', views.liste_matieres, name='liste'),
    path('ajouter/', views.ajouter_matiere, name='ajouter'),
    path('modifier/<int:id>/', views.modifier_matiere, name='modifier'),
]
