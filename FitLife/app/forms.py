from django import forms
from .models import PlanEntreno
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlanEntrenoForm(forms.ModelForm):
    class Meta:
        model = PlanEntreno
        fields = ['Entrenamiento', 'Valor', 'DuracionDias', 'Objetivo']
        widgets = {
            'Entrenamiento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tipo Entrenamiento'}),
            'Valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'DuracionDias': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en días'}),
            'Objetivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Objetivo'}),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'ContraseÃ±a'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalización de los widgets de los campos si es necesario
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Correo electrónico'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar contraseña'})