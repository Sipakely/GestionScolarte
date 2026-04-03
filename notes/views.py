from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from users.models import Etudiant

def ajouter_note(request):
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_notes')
    return render(request, 'notes/ajouter_note.html', {'form': form})

def moyenne_etudiant(etudiant_id):
    notes = Note.objects.filter(etudiant_id=etudiant_id)
    if notes.exists():
        total = sum(n.valeur for n in notes)
        return total / notes.count()
    return 0

def bulletin(request, etudiant_id):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    notes = Note.objects.filter(etudiant=etudiant)

    moyenne = moyenne_etudiant(etudiant_id)

    return render(request, 'notes/bulletin.html', {
        'etudiant': etudiant,
        'notes': notes,
        'moyenne': moyenne
    })