# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# localhost/instruments/instrument/[id]/
def instrument(req):

	context = {
		'instrument_name' : '[Instrument name]',
	}

	return render(req, 'html/instrument.html', context)
