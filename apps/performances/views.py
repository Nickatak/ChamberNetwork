from django.shortcuts import render
# from .models import Performance

# Create your views here.

def add(req):
	return render(req, 'html/add.html')

def upcoming(req):
	return render(req, 'html/upcoming.html')
