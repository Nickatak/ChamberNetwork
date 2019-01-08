from django.shortcuts import render, redirect
from .models import Member, Patron
from ..instruments.models import Instrument


def login_handler(req):

    if req.method == "POST":
        user, errors = Member.objects.validate_login(req.POST)
        if not errors:
            req.session['uid'] = user.pk
            return redirect('users:dashboard')
        else:
            req.session['errors'] = errors

    # Alright, to get this method to work, you're going to have to add a hidden next input field to return back to the same page, unless you want it to redirect somewhere else.
    return redirect(req.POST.get('next', 'public:login'))
    
    # Unless maybe we try this: return redirect(req.META.get('HTTP_REFERER', 'public:welcome'))


# houstonchambermusic.org/register_coach/
def register_coach(req):
    pass


# houstonchambermusic.org/register_member/
def register_member(req):
    if req.method == "POST":
        errors = Member.objects.new_member_validation(req.POST)

        if not errors:
            Member.objects.add_member(req.POST)
            return redirect('public:success')
        else:
            req.session['errors'] = errors
            req.session['old_data'] = req.POST

    return redirect('public:new_member')


# houstonchambermusic.org/register_patron/
def register_patron(req):
    if req.method == "POST":
        errors = Patron.objects.new_patron_validation(req.POST)

        if not errors:
            Patron.objects.add_patron(req.POST)
            return redirect('public:success')
        else:
            req.session['errors'] = errors

    return redirect('public:new_patron')


def dashboard(req):

    if 'uid' not in req.session:
        return redirect('public:welcome')

    context = {
        'user' : Member.objects.get(id=req.session['uid']),
        'instrument' :Instrument.objects.all(),
    }

    return render(req, 'html/dashboard.html', context)

def individual_member(req, member_id):

    if ('uid' not in req.session) or (not Member.objects.filter(id=member_id).exists()):
        return redirect('public:welcome')

    context = {
        'member' : Member.objects.get(id=member_id),
    }

    return render(req, 'html/individual_member.html', context)
