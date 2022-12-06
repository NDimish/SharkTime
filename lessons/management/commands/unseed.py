from django.core.management.base import BaseCommand, CommandError
from lessons.models import User,Student

from lessons.models import Lesson, Teacher, Student, LessonBook, LessonConfirmed, Payment, Sys_user, Sys_authority, \
    Sys_user_authority


from lessons.models import Lesson, Teacher, Student, LessonBook, LessonConfirmed, Payment, Sys_user, Sys_authority, \
    Sys_user_authority


class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.filter(is_superuser=False).delete()
        Student.objects.all().delete()

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

