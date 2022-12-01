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

#Student class 
class Student(models.Model):
    #unique student_id 
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name + " ID ("  + str(self.id) + ")")
    

#Admin class
class Admin(models.Model):
    #unique admin id 
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Director class 
class Director(models.Model):
    #unique admin id 
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()