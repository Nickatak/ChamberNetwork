from __future__ import unicode_literals

from django.shortcuts import render

# houstonchambermusic.org/public/welcome/
def welcome(req):
	return render(req, 'html/welcome.html')

# houstonchambermusic.org/public/register_member/
def register_member(req):
	return render(req, 'html/register_member.html')

# houstonchambermusic.org/public/register_coach/
def register_coach(req):
	return render(req, 'html/register_coach.html')

# houstonchambermusic.org/public/register_supporter
def register_supporter(req):
	return render(req, 'html/register_supporter.html')

# houstonchambermusic.org/public/about/
def about(req):
	return render(req, 'html/about.html')


