# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# houstonchambernet.org/musicians/logout/
def logout(req):
	pass

# houstonchambernet.org/musicians/musician/
def musician(req):
	return render(req, 'html/musician.html')

# houstonchambernet.org/musicians/dashboard/
def dashboard(req):
	return render(req, 'html/dashboard.html')




