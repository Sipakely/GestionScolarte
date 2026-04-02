from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        request.session['role'] = user.role

        return redirect('dashboard')

    return render(request, 'login.html', {'form': form})


def dashboard(request):
    role = request.session.get('role')
    return render(request, 'dashboard.html', {'role': role})


def logout_view(request):
    request.session.flush()
    return redirect('login')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant

# CREATE
def ajouter_etudiant(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        date_naissance = request.POST.get('date_naissance')
        classe = request.POST.get('classe')

        Etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            date_naissance=date_naissance,
            classe=classe
        )
        return redirect('liste_etudiants')

    return render(request, 'ajouter.html')


# READ
def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste.html', {'etudiants': etudiants})


# UPDATE
def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    if request.method == "POST":
        etudiant.nom = request.POST.get('nom')
        etudiant.prenom = request.POST.get('prenom')
        etudiant.email = request.POST.get('email')
        etudiant.date_naissance = request.POST.get('date_naissance')
        etudiant.classe = request.POST.get('classe')
        etudiant.save()

        return redirect('liste_etudiants')

    return render(request, 'modifier.html', {'etudiant': etudiant})


# DELETE
def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    etudiant.delete()
    return redirect('liste_etudiants')
