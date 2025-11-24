from django import forms
from .models import Viagem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ["destino", "data", "descricao"]

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
