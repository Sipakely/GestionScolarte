from django.shortcuts import render, redirect
from .forms import MatiereForm
from .models import Matiere

def ajouter_matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm()

    return render(request, 'templates matieres/form.html', {'form': form})


def modifier_matiere(request, id):
    matiere = Matiere.objects.get(id=id)

    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('liste_matieres')
    else:
        form = MatiereForm(instance=matiere)

    return render(request, 'template matieres/form.html', {'form': form})


def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'template matieres/liste.html', {'matieres': matieres})