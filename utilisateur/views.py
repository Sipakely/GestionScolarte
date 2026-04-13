from django.shortcuts import render, redirect
from .models import School, UserAccount


def signup_view(request):
    if request.method == "POST":
        school_name = request.POST.get("school_name")
        email = request.POST.get("email")
        username = request.POST.get("username")

        school, created = School.objects.get_or_create(
            email=email,
            defaults={"name": school_name}
        )

        if UserAccount.objects.filter(school=school).count() >= 3:
            return render(request, "signup.html", {
                "error": "Limite de 3 utilisateurs atteinte"
            })

        UserAccount.objects.create(
            school=school,
            username=username
        )

        return redirect("login")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")

        user = UserAccount.objects.filter(username=username).first()

        if user:
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Utilisateur introuvable"
        })

    return render(request, "login.html")