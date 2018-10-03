from __future__ import unicode_literals

from django.shortcuts import render

# localhost/public/welcome/
def welcome(req):
	return render(req, 'html/welcome.html')

# localhost/public/register_member/
def register_member(req):
	return render(req, 'html/register_member.html')

# localhost/public/register_coach/
def register_coach(req):
	return render(req, 'html/register_coach.html')

# localhost/public/about/
def about(req):
	return render(req, 'html/about.html')
