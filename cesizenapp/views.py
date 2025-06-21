from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.defaultfilters import length

from .forms import CreateInformationForm
from .models import Information

# Create your views here.

# @login_required
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


def home(request):
    informations = Information.objects.all()
    selected_category = request.GET.get('infoCategory')
    category_choices = Information.CATEGORY

    if not selected_category:
        selected_category = Information.CATEGORY[0][0]

    posts = Information.objects.filter(category=selected_category)
    post_length = posts.count()
    return render(request, 'home.html', {'informations': informations, 'posts': posts, 'selected_category': selected_category, 'category_choices': category_choices,'post_length': post_length})

def postInformation(request):
    if request.method == 'POST':
        form = CreateInformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully!")
            form = CreateInformationForm()
    else:
        form = CreateInformationForm()
    return render(request, 'postInformation.html', {'form': form, 'is_edit': False})

def edit_post(request, post_id):
    post = get_object_or_404(Information, idInformation=post_id)

    if request.method == 'POST':
        form = CreateInformationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Le post a été modifié avec succès.")
            return redirect('cesizenapp:home')
    else:
        form = CreateInformationForm(instance=post)

    return render(request, 'postInformation.html', {'form': form, 'is_edit': True})

from django.shortcuts import get_object_or_404

def delete_post(request, post_id):
    post = get_object_or_404(Information, idInformation=post_id)

    if request.user.is_superuser:
        post.delete()
        messages.success(request, "Le post a été supprimé avec succès.")
    else:
        messages.error(request, "Vous n'avez pas la permission de supprimer ce post.")

    return redirect('cesizenapp:home')