# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# houstonchambernet.org/musicians/logout/
def logout(req):
	pass

# houstonchambernet.org/musicians/musician/
def musician(req):

	context = {
		'page_name' : '[Musician name]',
	}

	return render(req, 'html/musician.html', context)

# houstonchambernet.org/musicians/dashboard/
def dashboard(req):

	context = {
		'page_name' : 'Dashboard',
	}

	return render(req, 'html/dashboard.html', context)




