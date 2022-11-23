from django.db import models
from django.contrib.auth.models import AbstractUser


#The User model 
class User(AbstractUser):
    USER_ROLES = (
        ('A', 'Administrator'),
        ('D', 'Director'),
        ('S', 'Student'),
    )

    role = models.CharField(max_length=1, blank=False, choices=USER_ROLES )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return '{}'.format(self.get_full_name())
