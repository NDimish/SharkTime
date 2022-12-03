# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# import uuid 


# #The User model 
# class User1(AbstractBaseUser):
#     USER_ROLES = (
#         ('A', 'Administrator'),
#         ('D', 'Director'),
#         ('S', 'Student'),
#     )

#     role = models.CharField(max_length=1, blank=False, choices=USER_ROLES )
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

    
#     def __str__(self):
#         return '{}'.format(self.get_full_name())

# #Student class 
# class Student(models.Model):
#     #unique student_id 
#     id = models.AutoField(primary_key=True)
#     #unique 4 digit student reference number
#     reference_number = models.UUIDField(primary_key=True, default=str(uuid.uuid4().int)[:6], editable=False,max_length=4)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#    # name = models.CharField(max_length=80, null=False, verbose_name="student name")
#     nick_name = models.CharField(max_length=500, null=True)
#     age = models.IntegerField(max_length=5, null=False)
#     email = models.CharField(max_length=500, null=False, verbose_name="user name or email address")
#     objects = models.Manager()
#     icon_url = models.CharField(max_length=500, null=True)
#     def __str__(self):
#         return (self.user.first_name + " " + self.user.last_name + " ID ("  + str(self.id) + ")")
    






# #Admin class
# class Admin(models.Model):
#     #unique admin id 
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

# #Director class 
# class Director(models.Model):
#     #unique admin id 
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = models.Manager()

