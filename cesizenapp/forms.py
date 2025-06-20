from django import forms
from django.contrib.auth.models import User
from cesizenapp.models import Information, Comment, Diagnostic

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'is_superuser']

class CreateInformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'content', 'caption', 'image', 'alt', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'color:red;'})
        }

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']