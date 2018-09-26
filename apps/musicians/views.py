# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# localhost/musicians/welcome/
def welcome(req):
	return render(req, 'html/welcome.html')

# localhost/musicians/register/
def register(req):
	return render(req, 'html/register.html')

# localhost/musicians/login/
def login(req):
	return render(req, 'html/login.html')
