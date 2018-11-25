from __future__ import unicode_literals

from django.shortcuts import render

from users.models import Member

def welcome(req):

	context = {
		'page_name' : 'Welcome',
	}

	return render(req, 'html/welcome.html', context)

def new_member_display(req):

	context = {
		'page_name' : 'Register Member',
	}

	return render(req, 'html/register_member.html', context)

def new_coach_display(req):

	context = {
		'page_name' : 'Register Coach',
	}

	return render(req, 'html/register_coach.html', context)

def new_patron_display(req):

	context = {
		'page_name' : 'Register Patron',
	}

	return render(req, 'html/register_patron.html', context)

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

# houstonchambermusic.org/new_member/
# def register_member(req):
# 	if request.method == "POST":
# 		errors = Member.objects.member_validation(request.POST)

# 		if not errors:
# 			Member.objects.add_member(request.POST)
# 			# not sure if this is the correct route:
# 			return redirect('/users/login')
# 		else:
# 			context = {
# 				'errors' : errors
# 			}
# 			return render(req, 'html/register_member.html', context=context)

# 	elif request.method == "GET":
# 		return render(req, 'html/register_member.html')


