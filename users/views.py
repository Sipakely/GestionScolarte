from django.shortcuts import render, redirect, get_object_or_404
from .forms import EtudiantForm
from .models import Etudiant
from django.contrib import messages
from matieres.models import Matiere
from notes.models import Note
from .models import School, UserAccount


# --------------------
# PAGE D'ACCUEIL
# --------------------
def index(request):
    return render(request, "index.html")


# --------------------
# DASHBOARD
# --------------------
def dashboard(request):
    context = {
        "total_etudiants": Etudiant.objects.count(),
        "total_matieres": Matiere.objects.count(),
        "total_notes": Note.objects.count(),
        "etudiants": Etudiant.objects.all()
    }
    return render(request, "dashboard.html", context)


# --------------------
# AJOUT ETUDIANT
# --------------------
def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Étudiant ajouté avec succès")
            return redirect('liste_etudiants')
        else:
            messages.error(request, "Erreur lors de l'ajout")
    else:
        form = EtudiantForm()

    return render(request, 'etudiants/form.html', {'form': form})


# --------------------
# MODIFIER ETUDIANT
# --------------------
def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification réussie")
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'etudiants/form.html', {'form': form})


# --------------------
# LISTE ETUDIANTS
# --------------------
def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste.html', {'etudiants': etudiants})


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