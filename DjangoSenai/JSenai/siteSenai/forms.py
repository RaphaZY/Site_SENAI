from django import forms
from django.forms import ModelForm
from .models import Cards, Usuarios

class CardsForm(forms.ModelForm):
    class Meta:

        model = Cards
        fields = "__all__"
        labels = {
            "title" : "Titulo",
            "preco": "Valor",
            "description": "Descrição",
            "path": "img", 
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Exel',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tempo de duração ...',
                }
            ),
            'preco': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '34.00',
                }
            ),

            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'foto',
                }
            )
        }

class UsuariosForms(forms.ModelForm):

    class Meta:

        model = Usuarios
        fields = "__all__"
        labels = {
            'nome': "identificação",
            'email': "endereço",
        }
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: Raphel",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: rapha@gmail.com",
                }
            )
        }