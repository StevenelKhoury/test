from django.db import models
from rest_hooks.signals import hook_event
# Create your models here.


class Utilisateur(models.Model):
    iduti = models.AutoField("num de l'utilisateur", primary_key=True)
    nom = models.CharField(max_length=40)
    prenom =models.CharField(max_length=40)
    user = models.ForeignKey('auth.User')
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


    def mark_as_read(self):
        # models can also have custom defined events
        
        hook_event.send(
            sender=self.__class__,
            event_name='utilisateur.added',
            obj=self 
        )





