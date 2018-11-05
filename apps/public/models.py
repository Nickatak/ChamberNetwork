# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import make_password, check_password

import re

NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

# Patron Manager Model
class PatronManager(models.Manager):
	pass

# Musician Manager Model
class MusicianManager(models.Manager):
	pass

# Patron Model
class Patron(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	phone_number = models.CharField(max_length=10)
	street_address = models.CharField(max_length=25)
	unit_number = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=5)

	# referred_by : does this belong here or in musician table?
	# referred_by = models.ForeignKey("Referred by", on_delete=models.CASCADE, related_name="musician")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = PatronManager()

# Musician Model
class Musician(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	# Password must be encrypted. Password is initially assigned at random. User can change once they are approved.
	password = models.CharField(max_length=25)
	street_address = models.CharField(max_length=25)
	unit_number = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=5)
	phone_number = models.CharField(max_length=10)

	# Primary and secondary instruments: FK set up correctly?
	# primary_instrument = models.ForeignKey("Primary instrument", on_delete=models.CASCADE, related_name="musicians")
	# secondary_instrument = models.ForeignKey("Secondary instrument", on_delete=models.CASCADE, related_name="musicians")

	# rating: only editable by admin. Values available are 1-5 or coach.
	rating = models.CharField(max_length=5)

	bio = models.TextField()

	# Approval : not sure about how to set this up. The idea is that it defaults to False but is changed to True by admin once musician is approved
	# approval = False

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = MusicianManager()




