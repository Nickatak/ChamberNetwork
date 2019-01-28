from django.shortcuts import redirect, render

from .models import Instrument
from ..users.models import Member


def individual_display(req, instrument_id):

    if 'uid' not in req.session:
        return redirect('public:welcome')

    if not Instrument.objects.filter(id=instrument_id).exists():
        return redirect('users:dashboard')

    this_instrument = Instrument.objects.get(id=instrument_id)
    context = {
        'all_instruments' : Instrument.objects.all(),
        'instrument' : this_instrument,
        'primary_users' : Member.objects.filter(primary_instrument__pk=instrument_id),
        'secondary_users' : Member.objects.filter(secondary_instrument__pk=instrument_id),
    }

    return render(req, 'html/individual_instrument.html', context)
