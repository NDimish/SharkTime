from django.db import models
from django.utils.timezone import now

# Create your models here.
class request(models.Model):
    request_status = (
        ('P', 'Pending'),
        ('R', 'Rejected'),
        ('A', 'Accepted'),
        ('O', 'Old'),
    )



    Teacher = models.CharField(max_length = 10)
    Student = models.CharField(max_length = 10)
    Date = models.DateField(default = now)
    time = models.DecimalField(decimal_places = 2, max_digits= 4)
    DateSent = models.DateField(default = now)
    status = models.CharField(max_length=1, blank=False, choices=request_status,default= 'O' )
    # for epic 2
    additionalInfo = models.TextField(default = "N/A")