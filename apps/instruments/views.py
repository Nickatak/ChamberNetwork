from django.shortcuts import render
from .models import Instrument

# Create your views here.

def dummy(req):
    pass

def individual_display(req, instrument_id):
    # Add a safeguard for this later.
    context = {
        'instrument' : Instrument.objects.get(id=int(instrument_id)),
    }
    return render(req, 'html/individual_instrument.html')