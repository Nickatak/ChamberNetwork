from django.shortcuts import render

# Create your views here.

def dummy(req):
    pass

def individual_instrument(req):
	return render(req, 'instruments:individual_instrument')