from django import forms
from .models import (
    Utilisateur
)

class Form_ajout_utilisateur(forms.Form):
    nom = forms.CharField(max_length=40, required=False)
    prenom = forms.CharField(max_length=40, required=False)
