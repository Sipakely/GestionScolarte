from django.shortcuts import render, redirect
from .models import Note
from users.models import Etudiant
from matieres.models import Matiere


def liste_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/liste.html', {'notes': notes})


def ajouter_note(request):
    etudiants = Etudiant.objects.all()
    matieres = Matiere.objects.all()

    if request.method == 'POST':
        etudiant_id = request.POST['etudiant']
        matiere_id = request.POST['matiere']
        valeur = request.POST['valeur']

        etudiant = Etudiant.objects.get(id=etudiant_id)
        matiere = Matiere.objects.get(id=matiere_id)

        Note.objects.create(
            etudiant=etudiant,
            matiere=matiere,
            valeur=valeur
        )

        return redirect('liste_notes')

    return render(request, 'notes/ajouter.html', {
        'users': etudiants,
        'matieres': matieres
    })