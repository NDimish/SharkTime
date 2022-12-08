from django.core.management.base import BaseCommand, CommandError
from lessons.models import User,Student, Term




from lessons.models import Lesson, Teacher, Student, Payment, Sys_user, Sys_authority, \
    Sys_user_authority


class Command(BaseCommand):
    def handle(self, *args, **options):
        Term.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        Student.objects.all().delete()
        Lesson.objects.all().delete()
        Teacher.objects.all().delete()
        Student.objects.all().delete()

        Payment.objects.all().delete()
        Sys_user.objects.all().delete()
        Sys_authority.objects.all().delete()
        Sys_user_authority.objects.all().delete()

