from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import CreateInformationForm, AccountForm
from .models import Information, Diagnostic

# Create your views here.

def home(request):
    user = request.user
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

STRESS_EVENTS = [
    ('Décès du conjoint', 100),
    ('Divorce', 73),
    ('Séparation conjugale', 65),
    ('Détention en prison ou dans une autre institution', 63),
    ('Décès d’un membre proche de la famille', 63),
    ('Blessure personnelle grave ou maladie', 53),
    ('Mariage', 50),
    ('Perte d’emploi (licenciement)', 47),
    ('Réconciliation conjugale', 45),
    ('Départ à la retraite', 45),
    ('Changement important dans la santé ou le comportement d’un membre de la famille', 44),
    ('Grossesse', 40),
    ('Problèmes sexuels', 39),
    ('Arrivée d’un nouveau membre dans la famille (naissance, adoption, emménagement d’un aîné, etc.)', 39),
    ('Réorientation professionnelle majeure', 39),
    ('Changement important de situation financière (nettement meilleur ou pire que d’habitude)', 38),
    ('Décès d’un ami proche', 37),
    ('Changement de domaine professionnel', 36),
    ('Changement important dans la fréquence des disputes avec le conjoint', 35),
    ('Souscription à un prêt hypothécaire (maison, entreprise, etc.)', 31),
    ('Saisie d’un bien immobilier ou d’un prêt', 30),
    ('Changement majeur de responsabilités au travail (promotion, rétrogradation, etc.)', 29),
    ('Départ du fils ou de la fille du domicile (mariage, études, armée, etc.)', 29),
    ('Conflits avec la belle-famille', 29),
    ('Réalisation personnelle remarquable', 28),
    ('Début ou fin d’un emploi du conjoint à l’extérieur du foyer', 26),
    ('Début ou fin de la scolarité', 26),
    ('Changement majeur dans les conditions de vie (nouveau logement, rénovation, détérioration, etc.)', 25),
    ('Révision des habitudes personnelles (habitudes vestimentaires, fréquentations, arrêt du tabac, etc.)', 24),
    ('Problèmes avec le supérieur hiérarchique', 23),
    ('Changement majeur des horaires ou conditions de travail', 20),
    ('Changement de résidence', 20),
    ('Changement d’établissement scolaire', 20),
    ('Changement important dans les loisirs habituels', 19),
    ('Changement important dans l’activité religieuse', 19),
    ('Changement important dans les activités sociales (clubs, cinéma, visites, etc.)', 18),
    ('Souscription à un prêt (voiture, téléviseur, congélateur, etc.)', 17),
    ('Changement majeur dans les habitudes de sommeil', 16),
    ('Changement important dans la fréquence des réunions familiales', 15),
    ('Changement majeur dans les habitudes alimentaires (quantité, horaires, environnement, etc.)', 15),
    ('Vacances', 13),
    ('Fêtes importantes', 12),
    ('Infractions mineures à la loi (excès de vitesse, traversée hors passage piéton, etc.)', 11),
]

def diagnostic(request):
    return render(request, 'diagnostic.html', {'events': STRESS_EVENTS})

@csrf_exempt
def submit_diagnostic(request):
    if request.method == "POST":
        try:
            selected_events = request.POST.getlist('events')
            score = sum(int(value) for value in selected_events)
        except Exception:
            return HttpResponseBadRequest("Invalid input")

        if score >= 300:
            result_msg = "Risque élevé : environ 80 % de chance d'un problème de santé majeur."
        elif 150 <= score < 300:
            result_msg = "Risque modéré : environ 50 % de chance d'un problème de santé majeur."
        else:
            result_msg = "Risque faible : faible probabilité de problème de santé majeur."

        show_save_button = request.user.is_authenticated

        html = render_to_string("diagnostic_result.html", {
            "score": score,
            "result_msg": result_msg,
            "show_save_button": show_save_button
        }, request=request)

        return HttpResponse(html)

    return HttpResponseBadRequest("Only POST allowed.")

@require_POST
@login_required
def save_diagnostic(request):
    score = request.POST.get("score")
    result_msg = request.POST.get("result_msg")

    if not score or not result_msg:
        return HttpResponseBadRequest("Invalid data")

    Diagnostic.objects.create(diagnosticUser=request.user, score=score, result=result_msg)
    messages.success(request, "Diagnostic enregistré.")
    return redirect('cesizenapp:diagnostic')

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