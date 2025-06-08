from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
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

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get(["username"]))
        user.email = request.POST.get(["email"])
        user.username = request.POST.get(["username"])
        user.password = request.POST.get(["password"])
        user.first_name = request.POST.get(["first_name"])
        user.last_name = request.POST.get(["last_name"])
        user.save()
    return render(request, 'signup.html')


