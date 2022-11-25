from django.test import TestCase

from lessons.models import Student

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        """ Create data, but this data will not actually insert data into the database table"""
        Student.objects.create(reference_number="10001",
                               name="Jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10002",
                               name="Jackson", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10003",
                               name="Tom", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10004",
                               name="Collin", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10005",
                               name="Ben", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")


        Student.objects.create(reference_number="10006",
                               name="Daniel", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10007",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

    def get_object(self):
        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="Jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)

        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="Jackson")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)

        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="Tom")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)


        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="Collin")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)


        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="Ben")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)

        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="Daniel")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)