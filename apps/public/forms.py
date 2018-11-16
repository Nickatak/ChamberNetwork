from django import forms

class MusicianLoginForm(forms.form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)