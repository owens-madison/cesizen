from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.modelForm):
    class meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'is_superuser']