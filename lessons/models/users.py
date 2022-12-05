from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


#The User model
class User(AbstractUser):
    
    username = models.CharField(
     max_length=60,
     unique=True
     # validators=[RegexValidator(
     # regex=r'^@\w{3,}$',
     # message='Username must consist of @ followed by at least three alphanumericals'
     # )]
    )

    role = models.CharField(max_length=50 )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=100)

    def __str__(self):
        return '{}'.format(self.get_full_name())

#Student class
class Students(models.Model):
    #unique student_id
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Admin class
class Admins(models.Model):
    #unique admin id
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Director class
class Directors(models.Model):
    #unique admin id
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
