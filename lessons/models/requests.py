from django.db import models
from django.utils.timezone import now

# Create your models here.
class request(models.Model):
    Teacher = models.CharField(max_length = 10)
    Student = models.CharField(max_length = 10)
    Date = models.DateField(default = now)
    time = models.DecimalField(decimal_places = 2, max_digits= 4)