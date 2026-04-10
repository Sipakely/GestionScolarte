from django.contrib import admin
from django.urls import path, include
from users.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', dashboard, name='dashboard'),

    path('users/', include('users.urls')),
    path('matieres/', include('matieres.urls')),
    path('notes/', include('notes.urls')),
]