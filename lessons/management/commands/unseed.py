from django.core.management.base import BaseCommand, CommandError
from lessons.models.requests import Weekday
from lessons.models import User,Student

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Weekday.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        Student.objects.all().delete()