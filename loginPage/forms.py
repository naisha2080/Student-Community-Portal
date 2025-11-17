from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

tailwind_input_classes = "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500"

class SignUpFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Remember me")