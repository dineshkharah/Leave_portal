from django.db import models

# Create your models here.


class savePortal(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    leaveType = models.CharField(max_length=250)
    startDate = models.CharField(max_length=250)
    endDate = models.CharField(max_length=250)
    reason = models.CharField(max_length=50)
