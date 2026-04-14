from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.liste_notes, name='liste'),
    path('ajouter/', views.ajouter_note, name='ajouter_note'),
    path('bulletin/<int:etudiant_id>/', views.bulletin_etudiant, name='bulletin'),
]
