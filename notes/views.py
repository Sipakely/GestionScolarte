from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Note
from .forms import NoteForm
from users.models import Etudiant
from utilisateur.models import School


# -------------------------
# RÉCUPÉRER ÉCOLE ACTIVE
# -------------------------
def get_active_school_name(request):
    school_id = request.session.get("school_id")
    school_username = request.session.get("school_username")

    school = None

    if school_id:
        school = School.objects.filter(id=school_id).first()

    if not school and school_username:
        school = School.objects.filter(username=school_username).first()

    if school:
        request.session["school_name"] = school.name
        return school.name

    return request.session.get("school_name", "")


# -------------------------
# AJOUT NOTE
# -------------------------
def ajouter_note(request):
    school_name = get_active_school_name(request)

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()  # la note est enregistrée directement

            messages.success(request, "Note ajoutée avec succès")
            return redirect("dashboard")

        else:
            messages.error(request, "Erreur lors de l'ajout de la note")

    else:
        form = NoteForm()

    return render(request, "Templates notes/form.html", {
        "form": form,
        "page_title": "Ajouter une note",
        "submit_label": "Enregistrer",
        "school_name": school_name,
    })


# -------------------------
# LISTE DES NOTES
# -------------------------
def liste_notes(request):
    school_name = get_active_school_name(request)

    notes = Note.objects.all()

    return render(request, "Templates notes/liste.html", {
        "notes": notes,
        "school_name": school_name
    })


# -------------------------
# BULLETIN ÉTUDIANT
# -------------------------
def bulletin_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    notes = Note.objects.filter(etudiant=etudiant)

    total = sum(note.valeur for note in notes)
    count = notes.count()

    moyenne = round(total / count, 2) if count > 0 else 0

    return render(request, "Templates notes/bulletin.html", {
        "etudiant": etudiant,
        "notes": notes,
        "moyenne": moyenne
    })