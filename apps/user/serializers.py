import json
import requests
from rest_framework import serializers
from .models import *
from env.mysiteWeb.mysiteWeb import settings
from test.dtracedata import instance



class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('nom','prenom')

def _send_to_zapier(request):
    url = getattr(settings, 'test', None)
    if url is None:
        url = request.META.get("HTTP_REFERER")
    

    data = {
        'utilisateur': instance.caller,
        'data': json.dumps(extdata),
    }

    resp = requests.post(
        settings.VMH_ZENSMS['jsp']['url'], data=data,
        auth=(settings.VMH_ZENSMS['jsp']['username'],
              settings.VMH_ZENSMS['jsp']['password']))
    