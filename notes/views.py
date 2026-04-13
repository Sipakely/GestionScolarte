from django.shortcuts import render, redirect
from .models import Note
from users.models import Etudiant
from matieres.models import Matiere
from utilisateur.models import School


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


def liste_notes(request):
    school_name = get_active_school_name(request)
    notes = Note.objects.filter(school_name=school_name) if school_name else Note.objects.none()
    return render(request, 'Templates notes/liste.html', {'notes': notes})


def ajouter_note(request):
    school_name = get_active_school_name(request)
    etudiants = Etudiant.objects.filter(school_name=school_name) if school_name else Etudiant.objects.none()
    matieres = Matiere.objects.filter(school_name=school_name) if school_name else Matiere.objects.none()

    if request.method == 'POST':
        etudiant_id = request.POST['etudiant']
        matiere_id = request.POST['matiere']
        valeur = request.POST['valeur']

        etudiant = Etudiant.objects.get(id=etudiant_id, school_name=school_name)
        matiere = Matiere.objects.get(id=matiere_id, school_name=school_name)

        Note.objects.create(
            school_name=school_name,
            etudiant=etudiant,
            matiere=matiere,
            valeur=valeur
        )

        return redirect('notes:liste')

    return render(request, 'Templates notes/ajouter.html', {
        'users': etudiants,
        'matieres': matieres
    })
