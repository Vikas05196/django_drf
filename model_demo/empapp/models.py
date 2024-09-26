from django.db import models

# Create your models here.
class Empapp(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=5)
    salary = models.FloatField()
    email = models.CharField(max_length=15)




