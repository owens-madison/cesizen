from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        user = (authenticate(request,
                             username=request.POST["username"],
                             password=request.POST["password"]))
        if user:
            auth_login(request, user)
            return redirect('cesizenapp:home')

        else:
            messages.error(request, 'log-in failed')
    return render(request, 'login.html')