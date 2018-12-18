from django.db import models

# Create your models here.

#Just a super basic model for now.
class Instrument(models.Model):
    name = models.TextField()
