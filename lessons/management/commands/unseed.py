from django.core.management.base import BaseCommand, CommandError
from lessons.models import User,Student

class Command(BaseCommand):
    def handle(self, *args, **options):

        User.objects.filter(is_superuser=False).delete()
        Student.objects.all().delete()