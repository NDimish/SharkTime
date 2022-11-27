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

    duration = (
        ('1', 60),
        ('2', 30),
        ('3', 45),
        ('4', 50),
    )



    Teacher = models.CharField(max_length = 10)
    Student = models.CharField(max_length = 10)
    Date = models.DateField(default = now)
    time = models.TimeField(default = now)
    DateSent = models.DateField(default = now)
    status = models.CharField(max_length=1, blank=False, choices=request_status,default= 'P' )
    objects = models.Manager()
    durations = models.CharField(max_length=1, blank=False, choices=duration,default= '1' )
    lesson_type = models.CharField(max_length=1000, blank=False, default='fuck serge')

    # for epic 2
    additionalInfo = models.TextField(default = "N/A")

    def isFulfilled(self):
        if(self.status=='A'):
            return True
        return False

    

