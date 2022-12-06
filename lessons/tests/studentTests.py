from django.test import TestCase

from lessons.models import Student, User

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        """ Create data, but this data will not actually insert data into the database table"""
        user1 = User.objects.create(#reference_number="10001",
                               first_name="Jack",
                               last_name = "Doe",
                               # age=18,
                               email="jackDoe@gmail.com",
                               role = 'S',
                               username = "jackD"
                              )
        student1 = Student(user=user1)
        #set the test student fields
        student1.created_at = "2022-11-24 10:30:28"
        student1.updated_at = "2022-11-24 10:30:28"
        student1.nick_name = "JDoe"
        student1.age = 18
        student1.icon_url = "/user/a.jpg"


    def get_object(self):
        result = User.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = User.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)
