# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# houstonchambermusic.org/performances/add/
def add(req):
	return render(req, 'html/add.html')

# houstonchambermusic.org/performances/performance/[id]/
def performance(req):
	return render(req, 'html/performance.html')

# houstonchambermusic.org/performances/calendar/
def upcoming(req):
	return render(req, 'html/upcoming.html')