from __future__ import unicode_literals

from django.shortcuts import render

from ..instruments.models import Instrument

def welcome(req):

	context = {
		'page_name' : 'Welcome',
	}

	return render(req, 'html/welcome.html', context)

def new_member_display(req):

	context = {
		'page_name' : 'Register Member',
        'errors' : req.session.pop('errors', None),
        'instruments' : Instrument.objects.all(),
        'old_data' : req.session.pop('old_data', None),
	}

	return render(req, 'html/register_member.html', context)

def new_coach_display(req):

	context = {
		'page_name' : 'Register Coach',
        'errors' : req.session.pop('errors', None),
        'instruments' : Instrument.objects.all(),
	}

	return render(req, 'html/register_coach.html', context)

def new_patron_display(req):

	context = {
		'page_name' : 'Register Patron',
	}

	return render(req, 'html/new_patron.html', context)

def about(req):

	context = {
		'page_name' : 'About Us',
	}

	return render(req, 'html/about.html', context)

def success(req):

	context = {
		'page_name' : 'Success',
	}

	return render(req, 'html/success.html', context)

def login_display(req):

	context = {
		'page_name' : 'Login',
	}

	return render(req, 'html/login.html', context)

