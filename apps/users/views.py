from django.shortcuts import render

from .models import Member

# Create your views here.

def login_handler(req):
    pass

# houstonchambermusic.org/new_member/
def register_member(req):
	if request.method == "POST":
		errors = Member.objects.new_validation(request.POST)

		if not errors:
			Member.objects.add_member(request.POST)
			return redirect('public:success')
		else:
			context = {
				'errors' : errors
			}
			return render(req, 'html/register_member.html', context=context)

	elif request.method == "GET":
		return redirect('public:register_member')