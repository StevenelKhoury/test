from django import forms


class AddUserForm(forms.Form):
    name = forms.CharField(max_length=40, required=False)
    firstname = forms.CharField(max_length=40, required=False)
