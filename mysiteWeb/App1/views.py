from django.shortcuts import render

from .models import (
    Utilisateur
)

from rest_framework import viewsets
from .models import *
from .serializers import *


from .forms import(
    Form_ajout_utilisateur
)

# Create your views here.

formulaire = Form_ajout_utilisateur(None)


def addUti(requete):
    contexte = {
        'titre': 'Ajout utilisateur',
        'formulaire': Form_ajout_utilisateur(),
        'nom_element': 'utilisateurs',
    }

    if requete.method == 'POST':
        formulaire = Form_ajout_utilisateur(requete.POST)
    else :
        formulaire = Form_ajout_utilisateur(None)

    if formulaire.is_valid():
        donnees = formulaire.cleaned_data       
        utilisateur = Utilisateur(**donnees)
        utilisateur.save(donnees)
    return render(requete, 'test.html', contexte)

#class UtilisateurViewSet(viewsets.modelViewSet):
#    queryset = Utilisateur.objects.all()
#    serializer_class=UtilisateurSerializer