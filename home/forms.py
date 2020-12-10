from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from home.models import Playlist
from home.models import Todo


class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['pic' , 'title' , 'description' , 'link']
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title' , 'status']