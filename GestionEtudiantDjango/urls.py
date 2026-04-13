from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from utilisateur import views as user_views


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    path('signup/', user_views.signup_view, name='signup'),
    path('login/', user_views.login_view, name='login'),
]