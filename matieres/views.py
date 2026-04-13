from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MatiereForm
from .models import Matiere
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

def ajouter_matiere(request):
    school_name = get_active_school_name(request)

    if request.method == 'POST':
        if not school_name:
            messages.error(request, "Aucun établissement actif trouvé pour cette session")
            return redirect('login')

        form = MatiereForm(request.POST)
        if form.is_valid():
            matiere = form.save(commit=False)
            matiere.school_name = school_name
            matiere.save()
            return redirect('matieres:liste')
    else:
        form = MatiereForm()

    return render(request, 'templates matiere/form.html', {
        'form': form,
        'page_title': "Ajouter une matière",
        'submit_label': "Enregistrer",
    })


def modifier_matiere(request, id):
    school_name = get_active_school_name(request)
    matiere = Matiere.objects.get(id=id, school_name=school_name)

    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            matiere = form.save(commit=False)
            matiere.school_name = school_name
            matiere.save()
            return redirect('matieres:liste')
    else:
        form = MatiereForm(instance=matiere)

    return render(request, 'templates matiere/form.html', {
        'form': form,
        'page_title': "Modifier matière",
        'submit_label': "Modifier",
    })


def liste_matieres(request):
    school_name = get_active_school_name(request)
    matieres = Matiere.objects.filter(school_name=school_name) if school_name else Matiere.objects.none()
    return render(request, 'templates matiere/liste.html', {'matieres': matieres})
