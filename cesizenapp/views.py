from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateInformationForm, AccountForm
from .models import Information


# Create your views here.

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

@login_required
def account(request):
    user = request.user

    if request.method == 'POST':
        if 'update_info' in request.POST:
            form = AccountForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Your account information has been updated successfully.")
                return redirect('cesizenapp:account')

        elif 'change_password' in request.POST:
            pass_form = PasswordChangeForm(user, request.POST)
            if pass_form.is_valid():
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                messages.success(request, "Your password has been changed successfully.")
                return redirect('cesizenapp:account')

        elif 'deactivate_account' in request.POST:
            user.is_active = False
            user.save()
            logout(request)
            messages.success(request, "Your account has been deactivated.")
            return redirect('login')
    else:
        form = AccountForm(instance=user)
        pass_form = PasswordChangeForm(user)

    return render(request, 'account.html', {
        'form': form,
        'pass_form': pass_form
    })

@login_required
def custom_logout(request):
    logout(request)
    return redirect('cesizenapp:login')

def admin_check(user):
    return user.is_superuser

class AdminUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    is_superuser = forms.BooleanField(required=False, label="Admin privileges")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser']

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('password')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user

@user_passes_test(admin_check)
def admin_user_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        users = User.objects.filter(username__icontains=search_query)
    else:
        users = User.objects.all().order_by('-is_superuser', 'username')

    return render(request, 'admin_users.html', {'users': users, 'search_query': search_query})

@user_passes_test(admin_check)
def admin_user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = AdminUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated.")
            return redirect('cesizenapp:admin_user_list')
    else:
        form = AdminUserForm(instance=user)
    return render(request, 'admin_user_edit.html', {'form': form, 'user_obj': user})

@user_passes_test(admin_check)
def admin_user_create(request):
    if request.method == 'POST':
        form = AdminUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created.")
            return redirect('cesizenapp:admin_user_list')
    else:
        form = AdminUserForm()
    return render(request, 'admin_user_create.html', {'form': form})

@user_passes_test(admin_check)
def admin_user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted.")
        return redirect('cesizenapp:admin_user_list')
    return render(request, 'admin_user_confirm_delete.html', {'user_obj': user})
