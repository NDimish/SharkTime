import datetime
import random
from lessons.models import Lesson, Teacher, Student
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("The seed command has not been implemented yet!")
        print("TO DO: Create a seed command following the instructions of the assignment carefully.")


# Set to global variables
specialList = ["piano", "violin", "guitar", "guitar", "drums", "saxophone", "cello", "flute"]


def seed_Lesson():
    faker = Faker("en_UK")
    for name in specialList:
        lesson = Lesson
        lesson.name = name
        lesson.lesson_num = 50  # how many the lesson num suitable?
        lesson.lesson_price = random("price")
        lesson.interval = random("interval")
        lesson.duration = "30,60,90"
        lesson.description = name
        lesson.create_time = datetime.datetime.now()
        lesson.update_time = datetime.datetime.now()


def seed_teacher():
    faker = Faker("en_UK")
    list_teacher_name = []
    for i in range(1, 101):
        teacher = Teacher()
        teacher.reference_number = faker.ean8()
        teacher.last_name = faker.last_name()
        teacher.email = faker.emal()
        teacher.title = faker.title()
        teacher.nick_name = faker.company()
        teacher.special = random_special()
        teacher.password = faker.password()
        teacher.create_time = datetime.datetime.now()
        teacher.update_time = datetime.datetime.now()
        # insert data to sqlite3 db
        Teacher.objects.update(teacher)


def seed_student():
    pass
    faker = Faker("en_UK")
    for i in range(1, 101):
        student = Student()
        student.reference_number = faker.ean8()
        student.first_name = faker.first_name()
        student.last_name = faker.last_name()
        student.birth_date = faker.date_of_birth()
        student.password = faker.password()
        student.email = faker.email()
        student.nick_name = faker.company()
        student.create_time = datetime.datetime.now()
        student.update_time = datetime.datetime.now()
        # insert data to sqlite3 db
        Student.objects.update(student)


def random_price():
    return round(random.uniform(5, 10), 1)


def random_special():
    # special list
    index = random.randint(0, 7)
    return specialList[index]


def random(type):
    if type == "price":
        return round(random.uniform(5, 10), 1)
    if type == "interval":
        return random.randint(1, 15)


random_price()