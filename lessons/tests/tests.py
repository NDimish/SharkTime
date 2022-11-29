from django.test import TestCase

from music.models import Student

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        """ Create data, but this data will not actually insert data into the database table"""
        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")


        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

        Student.objects.create(reference_number="10001",
                               name="jack", age=18,
                               email="hello@gmail.com",
                               nick_name="ramp",
                               icon_url="/user/a.jpg",
                               create_time="2022-11-24 10:30:28")

    def get_object(self):
        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)

        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)

        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)


        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)


        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)

        result = Student.objects.all().get()
        print(result)
        self.assertTrue(result.status)

        result = Student.objects.get(name="jack")
        self.assertEqual(result.age, 18)
        self.assertTrue(result.status)
        self.assertFalse(result.status)