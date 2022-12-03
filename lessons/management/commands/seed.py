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
        # user1.username = "itsjanedoe"     
        # user1.first_name = "Jane"
        # user1.last_name="Doe"
        # user1.role = 'S'
        # user1.email = "janeDoe@gmail.com"
        user1.save()

        student1 = Student( user=user1)
        student1.created_at = "2022-11-24 10:30:28"
        student1.updated_at = "2022-11-24 10:30:28"
        student1.nick_name = "JDoe"
        student1.age = 18
        student1.icon_url = "/user/a.jpg"
        student1.save()

# make example
def faker_data():
    # make 100 student info
    faker = Faker("en_UK")
    for i in range(1, 101):
        # geographic information
        address = faker.address()
        country = faker.country()
        country_code = faker.country_code()
        postcode = faker.postcode()

        # basic info
        email = faker.email()
        ssn = faker.ssn()
        bs = faker.bs()
        first_name_female = faker.first_name_female()
        first_name_male = faker.first_name_male()
        name = faker.name()
        phone_number = faker.phone_number()
        credit_card_number = faker.credit_card_number()

        # fake Encrypted information
        password = faker.password()
        md5 = faker.md5()

        random_int = faker.random_number(digits=10)

        print(str(random_int))


def fake_student():
    pass
    # faker = Faker("en_UK")
    # for i in range(1, 101):
    #     student = Student(
    #         name=faker.name(),
    #     )


faker_data()