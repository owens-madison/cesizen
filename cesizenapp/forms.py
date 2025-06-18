from django import forms
from django.contrib.auth.models import User
from cesizenapp.models import Information, Comment, Diagnostic

class CreateUserForm(forms.modelForm):
    class meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'is_superuser']

class CreateInformationForm(forms.modelForm):
    class meta:
        model = Information
        fields = ['title', 'content', 'caption', 'author', 'category', 'publicationDate']

class CreateCommentForm(forms.modelForm):
    class meta:
        model = Comment
        fields = ['comment', 'commenter', 'commentDate']

class CreateDiagnosticForm(forms.modelForm):
    class meta:
        model = Diagnostic
        fields = ['score', 'result', 'diagnosticDate', 'diagnosticUser']