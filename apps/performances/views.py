# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# localhost/performances/add/
def add(req):
	return render(req, 'html/add.html')