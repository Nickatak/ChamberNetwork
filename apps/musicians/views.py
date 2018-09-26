# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# localhost/musicians/welcome/
def welcome(req):
	return render(req, 'html/welcome.html')
