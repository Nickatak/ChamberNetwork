from django.shortcuts import render, redirect

from .models import Member

# Create your views here.

def login_handler(req):
    pass

# houstonchambermusic.org/new_member/
def register_member(req):
	if req.method == "POST":
		errors = Member.objects.new_member_validation(req.POST)

		if not errors:
			Member.objects.add_member(req.POST)
			return redirect('public:success')
		else:
			context = {
				'errors' : errors
			}
			return render(req, 'html/register_member.html', context=context)

	elif req.method == "GET":
		return redirect('public:register_member')

def register_patron(req):
	if req.method == "POST":
		errors = Patron.objects.new_patron_validation(req.POST)

		if not errors:
			Patron.objects.add_patron(req.POST)
			return redirect('public:success')
		else:
			context = {
				'errors' : errors
			}
			return render(req, 'html/register_patron.html', context=context)

	elif req.method == "GET":
		return redirect('public:register_patron')

