# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# houstonchambermusic.org/performances/add/
def add(req):

	context = {
		'page_name' : 'Add Performance'
	}

	return render(req, 'html/add.html', context)

# houstonchambermusic.org/performances/performance/[id]/
def performance(req):

	context = {
		'page_name' : 'Individual Performance'
	}

	return render(req, 'html/performance.html', context)

# houstonchambermusic.org/performances/calendar/
def upcoming(req):

	context = {
		'page_name' : 'Upcoming Performances'
	}

	return render(req, 'html/upcoming.html', context)