from django.db import models
from env.mysiteWeb.App1.forms import Form_ajout_utilisateur
#from rest_hooks.signals import hook_event
# Create your models here.


class Utilisateur(models.Model):
    iduti = models.AutoField("num de l'utilisateur", primary_key=True)
    nom = models.CharField(max_length=40)
    prenom =models.CharField(max_length=40)
    extra_data = models.JSONField()
   # user = property(lambda self: self.intermediary.user)

    def serialize_hook(self, hook):
        # optional, there are serialization defaults
        # we recommend always sending the Hook
        # metadata along for the ride as well
        
        return {
            'hook': hook.dict(),
            'data': {
                'id': self.id,
                'nom': self.nom,
                'prenom': self.prenom,
            }
        }

    def mark_as_add(self,requete):
        # models can also have custom defined events 
        formulaire = Form_ajout_utilisateur(requete.POST) 
        donnees = formulaire.cleaned_data  
        utilisateur=Utilisateur(**donnees)   
        hook_event.send(
            sender=self.post_save,
            event_name='utilisateur.added',
            obj=self 
        )





