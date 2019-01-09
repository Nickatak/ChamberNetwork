from django.shortcuts import render, redirect
from .models import Instrument


def individual_display(req, instrument_id):

    if 'uid' not in req.session:
        return redirect('public:welcome')

    if not Instrument.objects.filter(id=instrument_id).exists():
        return redirect('users:dashboard')

    context = {
        'instrument' : Instrument.objects.get(id=instrument_id),
    }

    return render(req, 'html/individual_instrument.html')