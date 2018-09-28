# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# localhost/musicians/welcome/
def welcome(req):
	return render(req, 'html/welcome.html')

# localhost/musicians/register_member/
def register_member(req):
	return render(req, 'html/register_member.html')

# localhost/musicians/login/
def login(req):
	return render(req, 'html/login.html')

# localhost/musicians/logout/
def logout(req):
	pass

# localhost/musicians/musician/
def musician(req):
	return render(req, 'html/musician.html')

# localhost/musicians/dashboard/
def dashboard(req):
	return render(req, 'html/dashboard.html')

# localhost/musicians/about/
def about(req):
	return render(req, 'html/about.html')

# localhost/musicians/contact/
def contact(req):
	return render(req, 'html/contact.html')


