from __future__ import unicode_literals

from django.shortcuts import render

from ..instruments.models import Instrument
from ..users.models import Member

def welcome(req):

	context = {
		'page_name' : 'Welcome',
	}

	return render(req, 'html/welcome.html', context)


def new_member_display(req):

	context = {
		'page_name' : 'Register Member',
        'errors' : req.session.pop('errors', None),
        'old_data' : req.session.pop('old_data', None),
        'instruments' : Instrument.objects.all(),
        'rating_choices' : Member.RATING_CHOICES,
	}

	return render(req, 'html/register_member.html', context)


def new_coach_display(req):

	context = {
		'page_name' : 'Register Coach',
        'errors' : req.session.pop('errors', None),
        'old_data' : req.session.pop('old_data', None),
        'instruments' : Instrument.objects.all(),
	}

	return render(req, 'html/register_coach.html', context)


def new_patron_display(req):

	context = {
		'page_name' : 'Register Patron',
        'errors' : req.session.pop('errors', None),
        'old_data' : req.session.pop('old_data', None),
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


def sponsors(req):

	context = {
		'page_name' : 'Sponsors',
	}

	return render(req, 'html/sponsors.html', context)


def resources(req):

	context = {
		'page_name' : 'Resources',
	}

	return render(req, 'html/resources.html', context)


def login_display(req):

	context = {
		'page_name' : 'Login',
        'old_data' : req.session.pop('old_data', None),
	}

	return render(req, 'html/login.html', context)


def request_reset(req):
    context = {
        'page_name' : 'Reset Password',
    }

    return render(req, 'html/pw_reset.html', context)


def token_sent(req):
    context = {
        'page_name' : 'Reset Password',
    }

    return render(req, 'html/token_sent.html', context)


def pw_reset_handler(req, reset_token):
    print('-' * 80)
    if ResetToken.objects.filter(value=reset_token).exists():
        print("RESET TOKEN FOUND")
    print('-' * 80)
    return redirect('public:welcome')

