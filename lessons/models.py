# from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser 
from django.db import models
 # Create your models here.
class User(AbstractUser):
    
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(max_length=50, blank=False,default='Student')

# Create your models here.
