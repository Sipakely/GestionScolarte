from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render
from .models import Etudiant


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'users/login.html', {
                    'form': form,
                    'error': 'Identifiants incorrects'
                })

    return render(request, 'users/login.html', {'form': form})


def dashboard(request):
    return render(request, 'users/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def liste_etudiants(request):
    return render(request, 'users/liste.html')

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'users/liste.html', {'etudiants': etudiants})

def dashboard(request):
    context = {
        'total_etudiants': Etudiant.objects.count(),
        'total_matieres': Matiere.objects.count(),
        'total_notes': Note.objects.count(),
    }
    return render(request, 'dashboard.html', context)