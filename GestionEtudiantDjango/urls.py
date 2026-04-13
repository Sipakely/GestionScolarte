from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from users import views as users_views
from utilisateur import views as user_views


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('dashboard/', users_views.dashboard, name='dashboard'),
    path('notes/', include('notes.urls')),
    path('matieres/', include('matieres.urls')),
    path('etudiants/', include('users.urls')),
    path('signup/', user_views.signup_view, name='signup'),
    path('login/', user_views.login_view, name='login'),
]
