from django.db import models

# Create your models here.

class Logfiles(models.Model):
    logfile = models.BinaryField()
