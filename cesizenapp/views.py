from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

@login_required
def home(request):
    user = request.user
    print(user.username)
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
    print("test")
    if request.method == 'POST':
        print(request.POST.get("email"))
        dataEmail = request.POST.get("email")
        dataUsername = request.POST.get("username")
        dataPassword = request.POST.get("password")
        dataFirst_name = request.POST.get("firstname")
        dataLast_name = request.POST.get("lastname")
        user = User.objects.create_user(email=dataEmail, username=dataUsername, password=dataPassword, first_name=dataFirst_name, last_name=dataLast_name, is_staff=False)
        user.save()
        return redirect('cesizenapp:login')
    return render(request, 'signup.html')


