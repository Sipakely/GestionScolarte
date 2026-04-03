from django.shortcuts import render, redirect, get_object_or_404
from .models import Matiere
from users.models import Etudiant

def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'matiere/liste.html', {'matieres': matieres})

def ajouter_matiere(request):
    etudiants = Etudiant.objects.all()

    if request.method == "POST":
        Matiere.objects.create(
            nom=request.POST['nom'],
            coefficient=request.POST['coefficient'],
            etudiant=Etudiant.objects.get(id=request.POST['etudiant'])
        )
        return redirect('liste_matieres')

    return render(request, 'matiere/ajouter.html', {'etudiants': etudiants})

def modifier_matiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    etudiants = Etudiant.objects.all()

    if request.method == "POST":
        matiere.nom = request.POST['nom']
        matiere.coefficient = request.POST['coefficient']
        matiere.etudiant = Etudiant.objects.get(id=request.POST['etudiant'])
        matiere.save()
        return redirect('liste_matieres')

    return render(request, 'matiere/modifier.html', {
        'matiere': matiere,
        'etudiants': etudiants
    })

def supprimer_matiere(request, id):
    matiere = get_object_or_404(Matiere, id=id)
    matiere.delete()
    return redirect('liste_matieres')