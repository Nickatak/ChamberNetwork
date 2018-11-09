from __future__ import unicode_literals

from django.shortcuts import render

# houstonchambermusic.org/public/welcome/
def welcome(req):

	context = {
		'page_name' : 'Welcome',
	}

	return render(req, 'html/welcome.html', context)

# houstonchambermusic.org/public/register_member/
def register_member(req):

	context = {
		'page_name' : 'Register Member',
	}

	return render(req, 'html/register_member.html', context)

# houstonchambermusic.org/public/register_coach/
def register_coach(req):

	context = {
		'page_name' : 'Register Coach',
	}

	return render(req, 'html/register_coach.html', context)

# houstonchambermusic.org/public/register_patron/
def register_patron(req):

	context = {
		'page_name' : 'Register Patron',
	}

	return render(req, 'html/register_patron.html', context)

# houstonchambermusic.org/public/about/
def about(req):

	context = {
		'page_name' : 'About Us',
	}

	return render(req, 'html/about.html', context)

# houstonchambermusic.org/public/success/
def success(req):

	context = {
		'page_name' : 'Success',
	}

	return render(req, 'html/success.html', context)

# houstonchambermusic.org/public/login/
def login(req):

	context = {
		'page_name' : 'Login',
	}

	return render(req, 'html/login.html', context)


