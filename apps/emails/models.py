from django.db import models

# Create your models here.




class EmailManager(models.Manager):
    pass



# Ideally, we can store templates for the emails here, but for now, I'm going to leave it blank.
class Email(models.Model):
    objects = EmailManager()