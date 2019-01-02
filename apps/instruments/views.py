from django.shortcuts import render

# Create your views here.

def dummy(req):
    pass

def individual_instrument(req, instrument_id):
    print(instrument_id)
    return render(req, 'html/individual_instrument.html')