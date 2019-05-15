from __future__ import unicode_literals
import re

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import model_to_dict

from ..emails.models import Email
from ..instruments.models import Instrument


NAME_REGEX = re.compile(r"^[a-zA-Z]+(?:[-\s.]+[a-zA-Z]+)*$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class MemberManager(models.Manager):


    def member_update(self, update_dict):
        update_dict['phone_number'] = update_dict.pop('tel1') + update_dict.pop('tel2') + update_dict.pop('tel3')
        user_id = update_dict.pop('id')
        pw = update_dict.pop('password')
        
        self.filter(pk=user_id).update(**update_dict) 
        
        user = self.get(pk=user_id)
        user.password = make_password(pw)
        user.save()


    def validate_edit(self, user_id, data):
        # The idea here is to use dicts to compare the changes, and then use our member validation to validate the fields.

        orig = model_to_dict(self.get(id=user_id))
        modded = False

        # Hard copy
        data = data.copy()

        # Remove CSRF token.
        data.pop('csrfmiddlewaretoken')

        # Normalize foreign keys (primary_instrument and secondary_instrument)
        data['primary_instrument'] = int(data['primary_instrument'])
        if not data['secondary_instrument']:
            data['secondary_instrument'] = None

        # Do a password validation if they've entered a PW to change.  If not, just pop both PW-keys.
        if data['new_password'] or data['confirm_password']:
            errors = self.validate_password(data['new_password'], data['confirm_password'])
            print(data['new_password'])
            if errors:
                return errors, orig
            else:
                pw = data['new_password']
                data.pop('new_password')
                data.pop('confirm_password')
                data['password'] = pw
        else:
            data.pop('new_password')
            data.pop('confirm_password')

        for key in data:
            # Explicit check against empty string.
            if data[key] != '' and orig[key] != data[key]:
                orig[key] = data[key]
                modded = True

        if modded:
            phone_number = orig.pop('phone_number')
            orig['tel1'] = phone_number[0:3]
            orig['tel2'] = phone_number[3:6]
            orig['tel3'] = phone_number[6:10]
            errors = self.new_member_validation(orig)
            expected_error = {'email' : 'Email already found in database. Either enter a different email or go to sign in page.'}
            if errors != expected_error:
                errors.pop('email')
                return errors, orig



        return None, orig


    def validate_login(self, data):
        email = data['email'].lower()
        attempted_password = data['password']

        user = None
        errors = {}

        if self.filter(email=email).exists():
            user = self.get(email=email)
            if not check_password(attempted_password, user.password):
                print('Working')
                errors['password'] = 'Username/Password combination not found, please try again or use the "Forgot Password" button below.'
        else:
            errors['password'] = 'Username/Password combination not found, please try again or use the "Forgot Password" button below.'

        return user, errors


    def new_member_validation(self, post_data, is_coach=False):
        errors = {}

        first_name = post_data['first_name']
        last_name = post_data['last_name']
        email = post_data['email'].lower()
        street_address = post_data['street_address']
        unit_number = post_data['unit_number']
        city = post_data['city']
        state = post_data['state']
        zip_code = post_data['zip_code']
        phone_number = post_data['tel1'] + post_data['tel2'] + post_data['tel3']
        bio = post_data['bio']
        area = post_data['area']

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

        if len(area) < 10:
            errors['area'] = 'Please provide area information (Minimum of 10 characters).'

        if (not is_coach) and 'rating' not in post_data:
            errors['rating'] = 'Please select a skill rating.'

        return errors


    def add_member(self, post_data, is_coach=False):
        first_name = post_data['first_name']
        last_name = post_data['last_name']
        email = post_data['email'].lower()
        street_address = post_data['street_address']
        unit_number = post_data['unit_number']
        city = post_data['city']
        state = post_data['state']
        zip_code = post_data['zip_code']
        area = post_data['area']
        phone_number = post_data['tel1'] + post_data['tel2'] + post_data['tel3']
        primary_instrument = Instrument.objects.get(pk=post_data['primary_instrument'])

        if ('secondary_instrument' in post_data) and (post_data['secondary_instrument'] != 'None'):
            secondary_instrument = Instrument.objects.get(pk=post_data['secondary_instrument'])
        else:
            secondary_instrument = None

        bio = post_data['bio']
        # Make this a choiceField later.
        if is_coach:
            rating = Member.PROFESSIONAL
        else:
            rating = post_data['rating']

        default_password = self.generate_new_password()
        self.create(
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            street_address=street_address,
                            unit_number=unit_number,
                            city=city,
                            state=state, 
                            zip_code=zip_code,
                            area=area,
                            phone_number=phone_number,
                            password=make_password(default_password),
                            primary_instrument=primary_instrument,
                            secondary_instrument=secondary_instrument,
                            bio=bio,
                            rating=rating,
                            is_coach=is_coach)

        return email, default_password


    def member_email_exists(self, email):
        return self.filter(email=email.lower()).exists()


    def generate_new_password(self):
        new_password = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567889")

        while self.validate_password(new_password, new_password):
            new_password = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567889")

        return new_password


    def get_all_with_instrument(self, instrument):
        return self.filter(models.Q(primary_instrument=instrument) | models.Q(secondary_instrument=instrument))


    def validate_password(self, password, confirm_password):
        errors = []

        if password != confirm_password:
            errors.append('Your passwords do not match eachother.')

        if len(password) < 8:
            errors.append('Your password must contain atleast eight characters.')

        if all(True if not char.isdigit() else False for char in password):
            errors.append('Your password must contain atleast one digit.')

        return errors


    def set_new_password(self, user_id, new_password):
        user = self.get(id=user_id)
        user.password = make_password(new_password)

        user.save()


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


class ResetTokenManager(models.Manager):

    def generate_new_token(self, email):
        if Member.objects.filter(email=email).exists():
            member = Member.objects.get(email=email)
        else:
            member = None

        if member:
            token_value = User.objects.make_random_password(length=32, allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567889")
            while self.filter(value=token_value).exists():
                token_value = User.objects.make_random_password(length=32, allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567889")

            return self.update_or_create(user=member, defaults= {'value' : token_value})[0]
        else:
            return None


class Member(models.Model):

    def save(self, *args, **kwargs):
        if self.id:
            old_obj = Member.objects.get(pk=self.id)
            if old_obj.is_approved == False and self.is_approved == True:
                token = ResetToken.objects.generate_new_token(self.email)
                Email.objects.send_approval_link(self.email, token.value)

        super(Member, self).save(*args, **kwargs)


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
    area = models.TextField()

    PROFESSIONAL = 0
    EXPERT = 1
    VERY_ADVANCED = 2
    ADVANCED = 3
    ADVANCED_INTERMEDIATE = 4
    INTERMEDIATE = 5
    ADVANCED_NOVICE = 6
    NOVICE = 7

#Professional, Expert, Very Advanced, Advanced, Advanced Intermediate, Intermediate, Advanced Novice, Novice
    RATING_CHOICES = (
        (PROFESSIONAL, "Professional"),
        (EXPERT, "Expert"),
        (VERY_ADVANCED, "Very Advanced"),
        (ADVANCED, "Advanced"),
        (ADVANCED_INTERMEDIATE, "Advanced Intermediate"),
        (INTERMEDIATE, "Intermediate"),
        (ADVANCED_NOVICE, "Advanced Novice"),
        (NOVICE, "Novice"),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


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


class ResetToken(models.Model):
    value = models.TextField()
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='password_tokens')

    created_at = models.DateTimeField(auto_now=True)
    objects = ResetTokenManager()

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
