from django.core.mail import send_mail
from django.db import models
from django.template import Template, Context

# Create your models here.




class EmailManager(models.Manager):
    def send_new_registration(self, email, password, is_coach):
        email_template = Template(self.get(name='New User Template').raw_template)

        raw_context = {
            'email' : email,
            'password' : password,
            'is_coach' : is_coach,
        }
        
        rendered_string = email_template.render(Context(raw_context))

        print(rendered_string)

        
        


# Ideally, we can store templates for the emails here, but for now, I'm going to leave it blank.
class Email(models.Model):
    name = models.CharField(max_length=255, unique=True)
    raw_template = models.TextField()
    objects = EmailManager()