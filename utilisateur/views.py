import time

from django.contrib.auth.hashers import check_password, make_password
from django.db import OperationalError, transaction
from django.shortcuts import render, redirect
from .models import School


def signup_view(request):
    if request.method == "POST":
        school_name = request.POST.get("school_name", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        if not username:
            return render(request, "signup.html", {
                "error": "Le nom d'utilisateur est obligatoire"
            })

        if not password:
            return render(request, "signup.html", {
                "error": "Le mot de passe est obligatoire"
            })

        for attempt in range(3):
            try:
                with transaction.atomic():
                    if School.objects.filter(email=email).exists():
                        return render(request, "signup.html", {
                            "error": "Email déjà utilisé"
                        })

                    if School.objects.filter(username=username).exists():
                        return render(request, "signup.html", {
                            "error": "Nom d'utilisateur déjà utilisé"
                        })

                    School.objects.create(
                        name=school_name,
                        email=email,
                        username=username,
                        password=make_password(password),
                    )
                break
            except OperationalError as exc:
                if "database is locked" not in str(exc).lower() or attempt == 2:
                    return render(request, "signup.html", {
                        "error": "Base de données occupée, réessaie dans quelques secondes."
                    })
                time.sleep(0.3)

        return redirect("login")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            return render(request, "login.html", {
                "error": "Nom d'utilisateur et mot de passe obligatoires"
            })

        school = School.objects.filter(username=username).first()

        if not school:
            return render(request, "login.html", {
                "error": "Nom d'utilisateur introuvable"
            })

        if not school.password:
            return render(request, "login.html", {
                "error": "Aucun mot de passe n'est défini pour ce compte"
            })

        password_valid = check_password(password, school.password) or school.password == password

        if password_valid:
            request.session["school_name"] = school.name
            request.session["school_username"] = school.username
            request.session["school_id"] = school.id
            request.session.modified = True
            return redirect("users:dashboard")

        return render(request, "login.html", {
            "error": "Mot de passe incorrect"
        })

    return render(request, "login.html")
