from django.shortcuts import redirect, render

from ..emails.models import Email
from ..instruments.models import Instrument
from .models import Member, Patron, ResetToken


def login_handler(req):

    if req.method == "POST":
        user, errors = Member.objects.validate_login(req.POST)
        if not errors:
            req.session['uid'] = user.pk
            return redirect('users:dashboard')
        else:
            req.session['errors'] = errors
            req.session['old_data'] = {
                                        'email' : req.POST['email'],
                                      }

    return redirect('public:login')


# houstonchambermusic.org/register_coach/
def register_coach(req):
    if req.method == "POST":
        errors = Member.objects.new_member_validation(req.POST, is_coach=True)

        if not errors:
            email, password = Member.objects.add_member(req.POST, is_coach=True)
            Email.objects.send_new_registration(email, password, is_coach=True)
            return redirect('public:success')
        else:
            req.session['errors'] = errors
            req.session['old_data'] = req.POST

    return redirect('public:new_coach')


# houstonchambermusic.org/register_member/
def register_member(req):
    if req.method == "POST":
        errors = Member.objects.new_member_validation(req.POST)

        if not errors:
            email, password = Member.objects.add_member(req.POST)
            Email.objects.send_new_registration(email, password)
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
            req.session['old_data'] = req.POST

    return redirect('public:new_patron')


def dashboard(req):

    if 'uid' not in req.session:
        return redirect('public:welcome')

    context = {
        'page_name' : 'Member Dashboard',
        'user' : Member.objects.get(id=req.session['uid']),
        'instruments' : Instrument.objects.all(),
    }

    return render(req, 'html/dashboard.html', context)


def individual_member(req, member_id):

    if ('uid' not in req.session) or (not Member.objects.filter(id=member_id).exists()):
        return redirect('public:welcome')

    context = {
        'page_name' : 'Member page',
        'member' : Member.objects.get(id=member_id),
        'instruments' : Instrument.objects.all(),
    }

    return render(req, 'html/individual_member.html', context)


def edit_member(req, member_id):

    if 'uid' not in req.session:
        return redirect('public:welcome')

    if req.method == 'POST':
        pass

    if int(member_id) != req.session['uid']:
        return redirect('users:dashboard')
    else:
        context = {
            'page_name' : 'Edit information',
            'user' : Member.objects.get(id=req.session['uid']),
            'instruments' : Instrument.objects.all(),
        }
        return render(req, 'html/edit_member.html', context)


def get_reset_token(req):
    if req.method == 'POST':
        if Member.objects.filter(email=req.POST['email']).exists():
            token = Member.objects.generate_new_token(email)
            Email.objects.send_token(email, token)

    return redirect('public:token_sent')


def pw_reset_handler(req, reset_token):
    print('-' * 80)
    print(reset_token)
    print('-' * 80)

def logout_handler(req):
    req.session.pop('uid', None)

    return redirect('public:welcome')
