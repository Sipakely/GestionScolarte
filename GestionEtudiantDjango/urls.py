from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from notes.views import accueil
from etudiants.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('users.urls')),
    path('matieres/', include('matieres.urls')),
    path('notes/', include('notes.urls')),
    path('', accueil),
    path('', dashboard, name='dashboard'),
]