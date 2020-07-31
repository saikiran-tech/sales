from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from salesrecord.models import Salesrecord

class SalesrecordForm(forms.ModelForm):
    class Meta:
        model = Salesrecord
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
