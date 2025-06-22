from django import forms
from django.contrib.auth.models import User
from cesizenapp.models import Information, StressEvent


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'is_superuser']

class CreateInformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'content', 'caption', 'image', 'alt', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'outline: none; background: none; border-color: black; border-width: 1px; border-style: solid; width: 500px; height: 35px; font-size: 101%; padding-left: 25px;'}),
            'caption': forms.TextInput(attrs={'style': 'outline: none; background: none; border-color: black; border-width: 1px; border-style: solid; width: 500px; height: 25px; padding-left: 25px;'}),
            'content': forms.Textarea(attrs={'style': 'outline: none; background: none; border: 1px solid black; width: 500px; height: 500px; padding: 10px; text-align: left; resize: none;'}),

            'alt': forms.TextInput(attrs={'style': 'outline: none; background: none; border-color: black; border-width: 1px; border-style: solid; width: 500px; height: 25px; padding-left: 25px;'}),
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

class StressEventForm(forms.ModelForm):
    class Meta:
        model = StressEvent
        fields = ['description', 'score']
