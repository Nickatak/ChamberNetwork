from django import forms
from .models import Musician

class MusicianLoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

def clean(self):
	data_dict = super().clean()

	if len(data_dict['username']) < 1:
			errors['username'] = 'You must enter a username.'

	if len(data_dict['password']) < 1:
		erros['password'] = "You must enter a password."

def login_musician(self):
	if username belongs to X and if password belongs to X:
		log in user
	else:
		do something else

