from django import forms

class MusicianLoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

def clean(self):
	data_dict = super().clean()

def login_validation(self, data_dict):

	if len(postData['username']) < 1:
			errors['username'] = 'You must enter a username.'

