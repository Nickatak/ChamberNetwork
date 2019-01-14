from __future__ import unicode_literals
import re

from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

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
        # Temporary holdover so dashboard is still available, but we can still proc errors purposely to test.
        else:
            errors['invalid'] = 'Invalid Credentials.'
            #if not check_password(attempted_password, user.password):
                # We can change this later, just let me know what you want it to say.
                #errors['invalid'] = 'Invalid credentials.'
        #else:
            ## We can change this later, just let me know what you want it to say.
            #errors['invalid'] = 'Invalid credentials.'
        
        return user, errors


    def new_member_validation(self, post_data, is_coach=False):
        errors = {}

        first_name = post_data['first_name']
        last_name = post_data['last_name']
        email = post_data['email']
        street_address = post_data['street_address']
        unit_number = post_data['unit_number']
        city = post_data['city']
        state = post_data['state']
        zip_code = post_data['zip_code']
        phone_number = post_data['tel1'] + post_data['tel2'] + post_data['tel3']
        bio = post_data['bio']

        if len(first_name) < 2:
            errors['first_name'] = 'First name must contain at least two characters.'
        elif not NAME_REGEX.match(first_name):
            errors['first_name'] = 'First name contains an invalid character.'

        if len(last_name) < 2:
            errors['last_name'] = 'Last name must contain at least two characters.'
        elif not NAME_REGEX.match(last_name):
            errors['last_name'] = 'Last name contains an invalid character.'

        if not EMAIL_REGEX.match(email):
            errors['email'] = 'Please enter a valid email address.'
        elif self.member_email_exists(email):
            errors['email'] = 'Email already found in database. Either enter a different email or go to sign in page.'

        if len(street_address) < 1:
            errors['street_address'] = 'Please enter your street address.'

        if len(city) < 1:
            errors['city'] = 'Please enter a city.'

        if len(zip_code) != 5:
            errors['zip_code'] = 'Please enter a valid US zip code.'

        if len(phone_number) != 10:
            errors['phone_number'] = 'Please enter a valid US phone number.'

        if 'primary_instrument' not in post_data:
            errors['primary_instrument'] = 'Please select a primary instrument.'

        if len(bio) < 1:
            errors['bio'] = 'Please provide a brief musical bio.'
        
        if (not is_coach) and 'rating' not in post_data:
            errors['rating'] = 'Please select a skill rating.'

        return errors


    def add_member(self, post_data, is_coach=False):
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        email = post_data['email']
        street_address = post_data['street_address']
        unit_number = post_data['unit_number']
        city = post_data['city']
        state = post_data['state']
        zip_code = post_data['zip_code']
        phone_number = post_data['tel1'] + post_data['tel2'] + post_data['tel3']
        primary_instrument = Instrument.objects.get(pk=post_data['primary_instrument'])
        
        if 'secondary_instrument'  in post_data: 
            secondary_instrument = Instrument.objects.get(pk=post_data['secondary_instrument'])
        else:
            secondary_instrument = None

        bio = post_data['bio']
        # Make this a choiceField later.
        if is_coach:
            rating = 'A'
        else:
            rating = post_data['rating']
        
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
                            secondary_instrument=secondary_instrument,
                            bio=bio,
                            rating=rating,
                            is_coach=is_coach)


    def member_email_exists(self, email):
        return self.filter(email=email).exists()


    # Very simple auto password generator for now.
    def generate_new_password(self):
        return User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")


    def get_all_with_instrument(self, instrument):
        return self.filter(models.Q(primary_instrument=instrument) | models.Q(secondary_instrument=instrument))


# Patron manager model:
class PatronManager(models.Manager):
    def new_patron_validation(self, post_data):
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        email = post_data['email']
        street_address = post_data['street_address']
        unit_number = post_data['unit_number']
        city = post_data['city']
        state = post_data['state']
        zip_code = post_data['zip_code']
        phone_number = post_data['tel1'] + post_data['tel2'] + post_data['tel3']

        errors = {}


        if len(first_name) < 2:
            errors['first_name'] = 'First name must contain at least two characters.'
        elif not NAME_REGEX.match(first_name):
            errors['first_name'] = 'First name contains an invalid character.'

        if len(last_name) < 2:
            errors['last_name'] = 'Last name must contain at least two characters.'
        elif not NAME_REGEX.match(last_name):
            errors['last_name'] = 'Last name contains an invalid character.'

        if not EMAIL_REGEX.match(email):
            errors['email'] = 'Please enter a valid email address.'
        elif self.patron_email_exists(email):
            errors['email'] = 'Email already found in database. Either enter a different email or go to sign in page.'

        if len(street_address) < 1:
            errors['street_address'] = 'Please enter your street address.'

        if len(city) < 1:
            errors['city'] = 'Please enter a city.'

        if len(zip_code) != 5:
            errors['zip_code'] = 'Please enter a valid US zip code.'

        # Ensure that a phone number is added:
        if len(phone_number) != 10:
            errors['phone_number'] = 'Please enter a valid US phone number.'

        return errors

    def add_patron(self, post_data):
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        email = post_data['email']
        street_address = post_data['street_address']
        unit_number = post_data['unit_number']
        city = post_data['city']
        state = post_data['state']
        zip_code = post_data['zip_code']
        phone_number = post_data['tel1'] + post_data['tel2'] + post_data['tel3']
        
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
    # email field is being used as login username for auth.
    email = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25, verbose_name="First Name")
    last_name = models.CharField(max_length=25, verbose_name="Last Name")
    street_address = models.CharField(max_length=25)
    unit_number = models.CharField(max_length=25, null=True, blank=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10, verbose_name="Phone Number")
    password = models.TextField()

    bio = models.TextField()
    rating = models.CharField(max_length=250, verbose_name="Skill Rating")


    # Instrument keys.
    primary_instrument = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, related_name='primary_users')
    secondary_instrument = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, related_name='secondary_users', blank=True)


    # Admin approval and coach status.
    is_approved = models.BooleanField(default=False, verbose_name="Has been approved")
    is_reviewed = models.BooleanField(default=False, verbose_name="Has been viewed")
    is_coach = models.BooleanField(default=False, verbose_name="Is a coach")
    has_default_password = models.BooleanField(default=False, verbose_name='Has set custom password')
    
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



