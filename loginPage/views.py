from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpFrom, CustomLoginForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpFrom()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form' : form})


def logout_view(request):
    logout(request)
    return redirect('login')