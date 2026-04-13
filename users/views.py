from django.shortcuts import render, redirect, get_object_or_404
from .forms import EtudiantForm
from .models import Etudiant
from django.contrib import messages
from django.db.models import Avg
from matieres.models import Matiere
from notes.models import Note
from utilisateur.models import School as ActiveSchool
from .models import School, UserAccount


def get_active_school_name(request):
    school_id = request.session.get("school_id")
    school_username = request.session.get("school_username")

    school = None
    if school_id:
        school = ActiveSchool.objects.filter(id=school_id).first()
    if not school and school_username:
        school = ActiveSchool.objects.filter(username=school_username).first()

    if school:
        request.session["school_name"] = school.name
        return school.name

    return request.session.get("school_name", "")


# --------------------
# PAGE D'ACCUEIL
# --------------------
def index(request):
    return render(request, "index.html")


# --------------------
# DASHBOARD
# --------------------
def dashboard(request):
    school_name = get_active_school_name(request)
    etudiants_qs = Etudiant.objects.filter(school_name=school_name) if school_name else Etudiant.objects.none()
    matieres_qs = Matiere.objects.filter(school_name=school_name) if school_name else Matiere.objects.none()
    notes_qs = Note.objects.filter(school_name=school_name) if school_name else Note.objects.none()
    moyenne_generale = notes_qs.aggregate(moyenne=Avg("valeur"))["moyenne"] or 0
    derniers_etudiants = etudiants_qs.order_by("-id")[:5]

    activites_recentes = []
    if notes_qs.exists():
        derniere_note = notes_qs.order_by("-id").first()
        activites_recentes.append(f"Note ajoutée: {derniere_note.etudiant.nom} - {derniere_note.matiere.nom}")
    if etudiants_qs.exists():
        dernier_etudiant = etudiants_qs.order_by("-id").first()
        activites_recentes.append(f"Étudiant inscrit: {dernier_etudiant.nom}")
    if matieres_qs.exists():
        derniere_matiere = matieres_qs.order_by("-id").first()
        activites_recentes.append(f"Matière active: {derniere_matiere.nom}")

    context = {
        "total_etudiants": etudiants_qs.count(),
        "total_matieres": matieres_qs.count(),
        "total_notes": notes_qs.count(),
        "moyenne_generale": round(moyenne_generale, 2),
        "etudiants": etudiants_qs,
        "derniers_etudiants": derniers_etudiants,
        "activites_recentes": activites_recentes,
        "school_name": school_name,
    }
    return render(request, "dashboard.html", context)


# --------------------
# AJOUT ETUDIANT
# --------------------
def ajouter_etudiant(request):
    school_name = get_active_school_name(request)

    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            etudiant = form.save(commit=False)
            etudiant.school_name = school_name
            etudiant.save()
            messages.success(request, "Étudiant ajouté avec succès")
            return redirect('users:liste')
        else:
            messages.error(request, "Erreur lors de l'ajout")
    else:
        form = EtudiantForm()

    return render(request, 'templates etudiant/form.html', {
        'form': form,
        'page_title': "Ajouter un étudiant",
        'submit_label': "Enregistrer",
    })


# --------------------
# MODIFIER ETUDIANT
# --------------------
def modifier_etudiant(request, id):
    school_name = get_active_school_name(request)
    etudiant = get_object_or_404(Etudiant, id=id, school_name=school_name)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            etudiant = form.save(commit=False)
            etudiant.school_name = school_name
            etudiant.save()
            messages.success(request, "Modification réussie")
            return redirect('users:liste')
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'templates etudiant/form.html', {
        'form': form,
        'page_title': "Modifier étudiant",
        'submit_label': "Modifier",
    })


# --------------------
# LISTE ETUDIANTS
# --------------------
def liste_etudiants(request):
    school_name = get_active_school_name(request)
    etudiants = Etudiant.objects.filter(school_name=school_name) if school_name else Etudiant.objects.none()
    return render(request, 'templates etudiant/liste.html', {'etudiants': etudiants})


# --------------------
# LOGIN SIMPLE
# --------------------
def login_view(request):
    if request.method == "POST":
        nom = request.POST.get("nom")

        request.session['user'] = nom

        return redirect('dashboard')

    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        school_name = request.POST.get('school_name')
        email = request.POST.get('email')
        username = request.POST.get('username')

        school, created = School.objects.get_or_create(
            email=email,
            defaults={'name': school_name}
        )

        user_count = UserAccount.objects.filter(school=school).count()

        if user_count >= 3:
            return render(request, 'signup.html', {
                'error': "Limite de 3 utilisateurs atteinte."
            })

        UserAccount.objects.create(
            school=school,
            username=username
        )

        return redirect('login')

    return render(request, 'signup.html')
