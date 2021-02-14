from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SearchMovieForm(forms.Form):
    search = forms.CharField(label='', max_length=25, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title of the Movie/TV series'}))

    year = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Release Year'}))


    choices = [('movie', 'MOVIES'),
               ('series', 'TV')]

    choice = forms.ChoiceField(label='', choices=choices, widget=forms.Select(
        attrs={'class': 'dropdown'}))
