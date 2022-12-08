import datetime
import random


from lessons.models import Lesson, Teacher, Student, Sys_user, Payment, Sys_authority, Sys_user_authority,  LessonBooking,  Term, \
    LessonRequest, User
from django.core.management.base import BaseCommand
from faker import Faker
from django_seed import Seed

Seeder = Seed.seeder()
import datetime as dt
import numpy as np
FORMAT =  "%Y-%m-%d"

# Set to global variables
specialList = ["piano", "violin", "guitar", "guitar", "drums", "saxophone", "cello", "flute"]


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB', 0)


    def handle(self, *args, **options):
        self.create_Terms()
        self.seed_teacher()
        self.seed_student()
        self.seed_Lesson()
       # self.seed_Sys_user()


# It is more accurate to use faker to write
# For more complex data we use faker to generate accurate test data


    def create_Terms (self):
        term1 = Term.objects.create(
        name =  "Term one",
        start_of_term_date = dt.datetime.strptime( "2022-09-01", FORMAT),
        end_of_term_date = dt.datetime.strptime( "2022-10-21", FORMAT)
        )
        term1.save()

        term2 = Term.objects.create(
        name =  "Term two",
        start_of_term_date = dt.datetime.strptime( "2022-10-31", FORMAT),
        end_of_term_date = dt.datetime.strptime( "2022-12-16", FORMAT)
        )
        term2.save()

        term3 = Term.objects.create(
        name =  "Term three",
        start_of_term_date = dt.datetime.strptime( "2023-01-03", FORMAT),
        end_of_term_date = dt.datetime.strptime( "2022-02-10", FORMAT)
        )
        term3.save()

        term4 = Term.objects.create(
        name =  "Term four",
        start_of_term_date = dt.datetime.strptime( "2023-02-20", FORMAT),
        end_of_term_date = dt.datetime.strptime( "2023-03-31", FORMAT)
        )
        term4.save()

        term5 = Term.objects.create(
        name =  "Term five",
        start_of_term_date = dt.datetime.strptime( "2023-04-17", FORMAT),
        end_of_term_date = dt.datetime.strptime( "2023-05-26", FORMAT)
        )
        term5.save()

        term6 = Term.objects.create(
        name =  "Term six",
        start_of_term_date = dt.datetime.strptime( "2023-06-05", FORMAT),
        end_of_term_date = dt.datetime.strptime( "2023-07-21", FORMAT)
        )
        term6.save()
        print ("Term Seeding Complete")



    def seed_teacher(self):

        list_teacher_name = []
        for i in range(1, 101):
            teacher = Teacher.objects.create(
            reference_number = self.faker.ean8(),
            email = self.faker.email(),
            title = self.random_title(),
            name = self.faker.last_name(),
            speciality = specialList[np.random.randint(0,8)])
            # insert data to sqlite3 db
            teacher.save()
        print("Teacher seeding complete")
    
    def seed_Lesson(self):

        for l_name in specialList:
            lesson = Lesson.objects.create(
                name = l_name,
                lesson_price = random.randint(30,100),
                duration = np.random.randint(1,4),

            )
            lesson.save()
        print("Lesson seeding complete")
      


    def seed_student(self):
        faker = Faker("en_UK")
        for i in range(1, 101):
            student_user = User.objects.create(
                role = "S",
                first_name = self.faker.first_name(),
                last_name = self.faker.last_name(),
                username  = self.faker.name(),
                email = self.faker.email(),
            )
            student_user.save()
            student = Student.objects.create(
                user = student_user,
                nick_name = self.faker.first_name(),
                age = np.random.randint(8,19)
            )
            student.save()
        print("Student seeding complete")


# # Put some ordered action data and some snapshots here
# def seed_lessonBook():
#     faker = Faker("en_UK")
#     for i in range(1, 101):
#         lessonbook = LessonBook()
#         lessonbook.lesson_id = self.faker.ean8()
#         lessonbook.lesson_name = random_special()
#         lessonbook.book_status = 1
#         lessonbook.booking_time = datetime.datetime.now()
#         lessonbook.student_id = self.faker.ean8()
#         lessonbook.create_time = datetime.datetime.now()
#         lessonbook.update_time = datetime.datetime.now()
#         LessonBook.objects.update(lessonbook)


# def seed_lessonConfirmed():
#     faker = Faker("en_UK")
#     for i in range(1, 101):
#         lessonconfirmed = LessonConfirmed()
#         lessonconfirmed.lesson_id = self.faker.ean8()
#         lessonconfirmed.teacher_id = self.faker.ean8()
#         lessonconfirmed.schedule_time = datetime.timedelta(days=2)
#         lessonconfirmed.finish_time = datetime.timedelta(days=2, hours=1)
#         lessonconfirmed.create_time = datetime.datetime.now()
#         lessonconfirmed.update_time = datetime.datetime.now()
#         LessonConfirmed.objects.update(lessonconfirmed)


    def random_price(self):
        return round(np.random.uniform(5, 10), 1)

    def random_title(self):
        return np.random.randint(1,5)

    def random_special(self):
        # special list
        index = random.randint(0, 7)
        return specialList[index]

    def random(type):
        if type == "price":
            return round(np.random.int(5, 10), 1)
        if type == "interval":
            return np.random.randint(1, 15)





    # # Here we use seed to automatically generate test data
    # def seed_Payment(self):
    #     # write like this ,it will add 10 numbers of Lesson data
    #     # we used seeder package

    #     Seeder.add_entity(Payment, 100)
    #     Seeder.execute()


    # def seed_Sys_user(self):
    #     # write like this ,it will add 10 numbers of Lesson data
    #     # we used seeder package
    #     Seeder.add_entity(Sys_user, 10)
    #     Seeder.execute(self)


    # def seed_Sys_authority(self):
    #     # write like this ,it will add 10 numbers of Lesson data
    #     # we used seeder package
    #     Seeder.add_entity(Sys_authority, 10)
    #     Seeder.execute()


    # def seed_Sys_user_authority(self):
    #     # write like this ,it will add 10 numbers of Lesson data
    #     # we used seeder package
    #     Seeder.add_entity(Sys_user_authority, 10)
    #     Seeder.execute()



        