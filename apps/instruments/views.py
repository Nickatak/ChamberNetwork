from django.shortcuts import render, redirect
from .models import Instrument
from ..users.models import Member
from django.db.models import Q


def individual_display(req, instrument_id):

    if 'uid' not in req.session:
        return redirect('public:welcome')

    if not Instrument.objects.filter(id=instrument_id).exists():
        return redirect('users:dashboard')

    this_instrument = Instrument.objects.get(id=instrument_id)
    context = {
        'instrument' : this_instrument,
        'members' : Member.objects.filter(Q(primary_instrument=this_instrument) | Q(secondary_instrument=this_instrument)),
    }

    return render(req, 'html/individual_instrument.html')