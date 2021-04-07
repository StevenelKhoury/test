import requests
from django.shortcuts import render

from .forms import AddUserForm
from .models import User


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
