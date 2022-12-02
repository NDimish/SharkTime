from django.core.management.base import BaseCommand, CommandError
from faker import Faker 
from lessons.models import User,Student
class Command(BaseCommand):
    
    def __init__(self):
        self.faker = Faker('en_GB')
    

    def handle( self, *args, **options):

        self.create_users()
        self.users = User.objects
        self.students = Student.objects.all()


    
    def create_users(self): 
        user1 = User.objects.create(role='S' , first_name = "Jane", last_name ="Doe",email = "janeDoe@gmail.com")
        user1.username = "itsjanedoe"     
        user1.first_name = "Jane"
        user1.last_name="Doe"
        user1.role = 'S'
        user1.email = "janeDoe@gmail.com"
        user1.save()

        student1 = Student( user=user1)
        student1.save()