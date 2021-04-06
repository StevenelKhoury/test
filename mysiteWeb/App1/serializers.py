#from rest_framework import serializers
from .models import *


class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('nom','prenom')

