from django.shortcuts import render
from ..instruments.models import Instrument
# from .models import Performance

# Create your views here.

def add(req):

	context = {
		'instruments' : Instrument.objects.all()
	}

	return render(req, 'html/add.html', context)

def upcoming(req):

	context = {
		'instruments' : Instrument.objects.all(),
	}

	return render(req, 'html/upcoming.html', context)
