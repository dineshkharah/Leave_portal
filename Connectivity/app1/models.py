from django.db import models

# Create your models here.


class savePortal(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=250, null=True)
    leaveType = models.CharField(max_length=250, null=True)
    startDate = models.CharField(max_length=250, null=True)
    endDate = models.CharField(max_length=250, null=True)
    reason = models.CharField(max_length=50, null=True)
