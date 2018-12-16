from django.shortcuts import render, redirect
from .models import Member, Patron


def login_handler(req):
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

	context = {

	}

	return render(req, 'html/dashboard.html', context)