# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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




