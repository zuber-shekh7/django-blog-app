from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserSignInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter password'
            }
        )
    )



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email',)


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image',)
    