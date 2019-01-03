from __future__ import unicode_literals
import re

from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.models import User

from ..instruments.models import Instrument


NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")




# Member Manager Model
class MemberManager(models.Manager):

    def validate_login(self, data):
        email = data['email']
        attempted_password = data['password']

        user = None
        errors = {}
        # Commented out validation for now so we can see the dashboard.
        if self.filter(email=email).exists():
            user = self.get(email=email)
            
            #if not check_password(attempted_password, user.password):
                # We can change this later, just let me know what you want it to say.
                #errors['invalid'] = 'Invalid credentials.'
        #else:
            ## We can change this later, just let me know what you want it to say.
            #errors['invalid'] = 'Invalid credentials.'
        
        return user, errors


    def new_member_validation(self, postData):

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
        elif self.member_email_exists(postData['email']) == True:
            errors['email'] = 'Email already found in database. Either enter a different email or go to sign in page.'

        # Ensure that a street address is added:
        if len(postData['street_address']) < 1:
            errors['street_address'] = 'Please enter your street address.'

        # Ensure that a city is added:
        if len(postData['city']) < 1:
            errors['city'] = 'Please enter a city.'

        # Ensure that a zip code is added:
        if len(postData['zip_code']) < 1:
            errors['zip_code'] = 'Please enter your zip code.'

        # Ensure that a phone number is added:
        if len(postData['phone_number']) < 10:
            errors['phone_number'] = 'Please enter a valid phone number.'

        # Ensure that a primary instrument is chosen:
        if len(postData['primary_instrument']) < 1:
            errors['primary_instrument'] = 'Please select a primary instrument.'

        # Ensure that a primary instrument is chosen:
        if len(postData['bio']) < 1:
            errors['bio'] = 'Please provide a brief musical bio.'

        return errors

    def add_member(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        street_address = data['street_address']
        unit_number = data['unit_number']
        city = data['city']
        state = data['state']
        zip_code = data['zip_code']
        phone_number = data['phone_number']
        primary_instrument = data['primary_instrument']
        second_instrument = data['second_instrument']
        bio = data['bio']
        # For rating, we need to "pop" just the first character of each rating, ie the number, not the description
        rating = data['rating']
        
        return self.create(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            street_address=street_address,
                            unit_number=unit_number,
                            city=city,
                            state=state, 
                            zip_code=zip_code,
                            phone_number=phone_number,
                            primary_instrument=primary_instrument,
                            second_instrument=second_instrument,
                            bio=bio,
                            rating=rating)

    def member_email_exists(self, email):
        return self.filter(email=email).exists()

# Patron manager model:
class PatronManager(models.Manager):
    def new_patron_validation(self, postData):

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
        elif self.patron_email_exists(postData['email']) == True:
            errors['email'] = 'Email already found in database. Either enter a different email or go to sign in page.'

        # Ensure that a street address is added:
        if len(postData['street_address']) < 1:
            errors['street_address'] = 'Please enter your street address.'

        # Ensure that a city is added:
        if len(postData['city']) < 1:
            errors['city'] = 'Please enter a city.'

        # Ensure that a zip code is added:
        if len(postData['zip_code']) < 1:
            errors['zip_code'] = 'Please enter your zip code.'

        # Ensure that a phone number is added:
        if len(postData['phone_number']) < 10:
            errors['phone_number'] = 'Please enter a valid phone number.'

        return errors

    def add_patron(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        street_address = data['street_address']
        unit_number = data['unit_number']
        city = data['city']
        state = data['state']
        zip_code = data['zip_code']
        phone_number = data['phone_number']
        
        return self.create(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            street_address=street_address,
                            unit_number=unit_number,
                            city=city,
                            state=state,
                            zip_code=zip_code,
                            phone_number=phone_number)

    def patron_email_exists(self, email):
        return self.filter(email=email).exists()

# Member Model
class Member(models.Model):
    #Will the email be used as auth?
    email = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25, verbose_name="First Name")
    last_name = models.CharField(max_length=25, verbose_name="Last Name")
    street_address = models.CharField(max_length=25)
    unit_number = models.CharField(max_length=25, null=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10, verbose_name="Phone Number")
    password = models.TextField()

    is_coach = models.BooleanField(default=False, verbose_name="Is a coach")

    # Instruments are not set up correctly, because they need to interact (as FK) with instrument table
    primary_instrument = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, related_name='primary_users')
    second_instrument = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, related_name='secondary_users')
    bio = models.TextField()
    rating = models.CharField(max_length=250, verbose_name="Skill Rating")

    # Approval : not sure about how to set this up. The idea is that it defaults to False but is changed to True by admin once musician is approved
    is_approved = models.BooleanField(default=False, verbose_name="Has been approved")
    is_reviewed = models.BooleanField(default=False, verbose_name="Has been viewed")

    # Primary and secondary instruments: FK set up correctly?
    # primary_instrument = models.ForeignKey("Primary instrument", on_delete=models.CASCADE, related_name="musicians")
    # secondary_instrument = models.ForeignKey("Secondary instrument", on_delete=models.CASCADE, related_name="musicians")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Application Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last updated")

    objects = MemberManager()

# Patron Model. Merely an email list. For now, OK to just store information. But eventually we need to program the site to do something with the emails - either email Patrons automatically or at least send the emails to Michael.
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



