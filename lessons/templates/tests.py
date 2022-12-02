from django.test import TestCase
from .models import User

class UserModelTestCase(TestCase):
    def test_valid_user(self):
        user=User.objects.create_user(

        first_name='John',last_name='Doe',email='johndoe@example.org'
        ,password='Password123',role='Student'
        )
        try:
            user.full_clean()
        except (ValidationError):
            self.fail('Test User should be valid')

    # def test_valid_user(self):
    #     user=User.objects.create_user(
    #
    #     first_name='John',last_name='Doe',email='johndoe@example.org'
    #     ,password='Password123',role='Student'
    #     )
    #     try:
    #         user.full_clean()
    #     except (ValidationError):
    #         self.fail('Test User should be valid')
