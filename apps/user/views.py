import json
import os
import requests

#import telegram

from django.http import JsonResponse
#from django.view import View 

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.shortcuts import render

#from django.conf import settings

#from ipware.ip import get_ip


from .forms import AddUserForm
from .models import User

#URL=settings.BOT_URL
#my_token = settings.BOT_TOKEN
#my_chat_id= settings.BOT_CHAT_ID
'''

class LazyEncoder(DjangoJSONEncoder):
    def default(self,obj):
        if isinstance(obj,dict):
            return str(obj)
        return super().default(obj)

def bot(request,msg,chat_id=my_chat_id,token=my_token):
    bot=telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id,text=msg)

def home(request):
    if request.user.is_anonymous:
        bot(request,str(get_ip(request)))
    else:
        bot(request,serialize('json',User.objects.filter(username=request.user),fields=('username'),cls=LazyEncoder))
'''

TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = os.getenv("TUTORIAL_BOT_TOKEN", "error_token")

'''class dejesaispas(View):
    def post(self, request, *args, **kwargs):
        t_data= json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]

        try:
            text = t_message["text"].strip().lower()
        except Exception as e:
            return JsonResponse({"ok": "POST request processed"})

        text = text.lstrip("/")
        chat = tb_tutorial_collection.find_one({"chat_id": t_chat["id"]})
        if not chat:
            chat = {
                "chat_id": t_chat["id"],
                "counter": 0
            }
            response = steven_collection.insert_one(chat)
            # we want chat obj to be the same as fetched from collection
            chat["_id"] = response.inserted_id

        if text == "+":
            chat["counter"] += 1
            tb_tutorial_collection.save(chat)
            msg = f"Number of '+' messages that were parsed: {chat['counter']}"
            self.send_message(msg, t_chat["id"])
        elif text == "restart":
            blank_data = {"counter": 0}
            chat.update(blank_data)
            tb_tutorial_collection.save(chat)
            msg = "The Tutorial bot was restarted"
            self.send_message(msg, t_chat["id"])
        else:
            msg = "Unknown command"
            self.send_message(msg, t_chat["id"])

        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
        )

'''

def _send_user(user):
    data = {
        'id': user.id,
        'name': user.firstname + ' ' + user.name
    }
    response = requests.post('http://httpbin.org/post', data=data)
    print('RESPONSE', response)


def add_user(request):
    form = AddUserForm()
    msg = None

    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid() is True:
            data = form.cleaned_data
            data['extra_data'] = {}
            user = User(**data)
            user.save(data)
            _send_user(user)
            msg = 'Envoi OK'
    context = {
        'titre': 'Ajout utilisateur',
        'formulaire': form,
        'nom_element': 'utilisateurs',
        'msg': msg
    }
    return render(request, 'test.html', context)



# class UtilisateurViewSet(viewsets.modelViewSet):
#    queryset = Utilisateur.objects.all()
#    serializer_class=UtilisateurSerializer
