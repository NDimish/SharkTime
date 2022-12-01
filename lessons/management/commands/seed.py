from django.core.management.base import BaseCommand, CommandError
from faker import Faker 
from lessons.models.requests import Weekday
from lessons.models import User,Student
class Command(BaseCommand):
    
    def __init__(self):
        self.faker = Faker('en_GB')
    

    def handle( self, *args, **options):
        # self.create_weekdays()
        # self.weekdays = Weekday.objects.all()

        self.create_users()
        self.users = User.objects
        self.students = Student.objects.all()

    def create_weekdays(self):
        day1 = Weekday.objects.create(day = Weekday.MONDAY)
        day1.save()

        day2 = Weekday.objects.create(day = Weekday.TUESDAY)
        day2.save()

        day3 = Weekday.objects.create(day = Weekday.WEDNESDAY)
        day3.save()

        day4 = Weekday.objects.create(day = Weekday.THURSDAY)
        day4.save()

        day5 = Weekday.objects.create(day = Weekday.FRIDAY)
        day5.save()

        print("Weekday seeding complete")
    
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