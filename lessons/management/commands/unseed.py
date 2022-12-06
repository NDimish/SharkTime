from django.core.management.base import BaseCommand, CommandError

from lessons.models import Lesson, Teacher, Student, LessonBook, LessonConfirmed, Payment, Sys_user, Sys_authority, \
    Sys_user_authority


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("The unseed command has not been implemented yet!")
        print("TO DO: Create an unseed command following the instructions of the assignment carefully.")

def unseed():
    Lesson.objects.all().delete()
    Teacher.objects.all().delete()
    Student.objects.all().delete()
    LessonBook.objects.all().delete()
    LessonConfirmed.objects.all().delete()
    Payment.objects.all().delete()
    Sys_user.objects.all().delete()
    Sys_authority.objects.all().delete()
    Sys_user_authority.objects.all().delete()

