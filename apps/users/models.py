from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User



# Patron Model. This is just for an emailing list right?  All we need to do is store them then, not a big deal.
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


# Musician Manager Model
class MusicianManager(models.Manager):
    def validate_login(self, data):
        

# Musician Model
class Musician(models.Model):
    #Will the email be used as auth?
    email = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10)
    street_address = models.CharField(max_length=25)
    unit_number = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    bio = models.TextField()

    # Approval : not sure about how to set this up. The idea is that it defaults to False but is changed to True by admin once musician is approved
    is_approved = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)

    # Primary and secondary instruments: FK set up correctly?
    # primary_instrument = models.ForeignKey("Primary instrument", on_delete=models.CASCADE, related_name="musicians")
    # secondary_instrument = models.ForeignKey("Secondary instrument", on_delete=models.CASCADE, related_name="musicians")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MusicianManager()
