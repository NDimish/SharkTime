from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from lessons.models.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("The seed command has not been implemented yet!")
        print("TO DO: Create a seed command following the instructions of the assignment carefully.")


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
