from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import User

SERVER_EMAIL = 'admin@ntakemori.com'

class EmailManager(models.Manager):
    def send_new_registration(self, email, password, is_coach=False):
        context = {
            'email' : email,
            'password' : password,
            'is_coach' : is_coach,
        }

        rendered_string = render_to_string("email_templates/New_User_Template.html", context)
        print('-' * 80)
        print(rendered_string)
        print('-' * 80)
        admin_emails = [user.email for user in User.objects.filter(is_superuser=True)]
        
        subj = 'HCMN: New User Registered.'
        message = rendered_string
        
        send_mail(subj, message, SERVER_EMAIL, admin_emails)
        


    def send_pw_reset_link(self, email, reset_token, domain_name):
        context = {
            'reset_url' : domain_name + reverse('public:pw_reset_display', args=[reset_token]),
        }

        rendered_string = render_to_string("email_templates/Pass_Reset_Template.html", context)
        print('-' * 80)
        print(rendered_string)
        print('-' * 80)
        admin_emails = [user.email for user in User.objects.filter(is_superuser=True)]


# Ideally, we can store templates for the emails here, but for now, I'm going to leave it blank.
class Email(models.Model):
    name = models.CharField(max_length=255, unique=True)
    raw_template = models.TextField()
    objects = EmailManager()
