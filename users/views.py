from django.shortcuts import render, redirect
from .forms import EtudiantForm
from .models import Etudiant

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()

    return render(request, 'etudiants/form.html', {'form': form})


def modifier_etudiant(request, id):
    etudiant = Etudiant.objects.get(id=id)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'etudiants/form.html', {'form': form})


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste.html', {'etudiants': etudiants})