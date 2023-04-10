from django.db import models


class LeaveApplication(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    leave_type = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.name
