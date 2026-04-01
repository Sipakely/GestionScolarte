from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        request.session['role'] = user.role

        return redirect('dashboard')

    return render(request, 'login.html', {'form': form})


def dashboard(request):
    role = request.session.get('role')
    return render(request, 'dashboard.html', {'role': role})


def logout_view(request):
    request.session.flush()
    return redirect('login')
