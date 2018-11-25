from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.models import User

import re

NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


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


# Member Manager Model
class MemberManager(models.Manager):
    '''
    def validate_login(self, data):
        email = data['email']
        attempted_password = data['password']
        
        if self.filter(email=email).exists():
            user = self.get(email=email)
            
            if check_password(attempted_password, user.password):
    '''

    def new_validation(self, postData):

        errors = {}


        # Ensure that first name 1) has content 2) is at least 2 characters long and 3) contains no invalid characters:
        if len(postData['first_name']) < 1:
            errors['first_name'] = 'You must enter a first name.'
        elif len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must contain at least two characters.'
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = 'First name contains an invalid character.'

        # Ensure that last name 1) has content 2) is at least 2 characters long and 3) contains no invalid characters:
        if len(postData['last_name']) < 1:
            errors['last_name'] = 'You must enter a last name.' 
        elif len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must contain at least two characters.'
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = 'Last name contains an invalid character.'

        # Ensure that email field is completed and that email adheres to standard conventions:
        if len(postData['email']) < 1:
            errors['email'] = 'You must enter an email address.'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email address.'
        # Call email_exists to ensure they haven't already signed up
        elif self.email_exists(postData['email']) == True:
            errors['email'] = 'Email already found in database. Either enter a different email or go to sign in page.'

        return errors

    def add_member(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        return self.create(first_name=first_name, last_name=last_name, email=email)


# Member Model
class Member(models.Model):
    #Will the email be used as auth?
    email = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    # phone_number = models.CharField(max_length=10)
    # street_address = models.CharField(max_length=25)
    # unit_number = models.CharField(max_length=25)
    # city = models.CharField(max_length=25)
    # state = models.CharField(max_length=2)
    # zip_code = models.CharField(max_length=5)

    # bio = models.TextField()

    # Approval : not sure about how to set this up. The idea is that it defaults to False but is changed to True by admin once musician is approved
    # is_approved = models.BooleanField(default=False)
    # is_reviewed = models.BooleanField(default=False)

    # Primary and secondary instruments: FK set up correctly?
    # primary_instrument = models.ForeignKey("Primary instrument", on_delete=models.CASCADE, related_name="musicians")
    # secondary_instrument = models.ForeignKey("Secondary instrument", on_delete=models.CASCADE, related_name="musicians")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MemberManager()
