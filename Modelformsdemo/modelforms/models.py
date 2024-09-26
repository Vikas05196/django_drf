from django.db import models


# Create your models here.

class Project(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()
    name = models.CharField(max_length=25)
    assignedto = models.CharField(max_length=20)
    priority = models.IntegerField(("10"))
