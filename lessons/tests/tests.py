import datetime
import unittest

from lessons.models import Student, Teacher, Lesson, LessonBook


class MyTestCase(unittest.TestCase):
    def test_student(self):
        """student test"""
        student = Student.objects.create(
            reference_number="10001",
            name="jack", age=18,
            email="hello@gmail.com",
            nick_name="ramp",
            icon_url="/user/a.jpg",
            create_time="2022-11-24 10:30:28")

        self.assertIsNotNone(student)

        rows = Student.objects.update(
            reference_number="10001",
            name="jack", age=18,
            email="hello@gmail.com",
            nick_name="ramp",
            icon_url="/user/a.jpg",
            create_time="2022-11-24 10:30:28")

        self.assertNotEqual(rows == 0)  # add assertion here

        count = Student.objects.all().acount()
        self.assertNotEqual(count == 0)

        delete = Student.objects.all().first().delete()
        self.assertNotEqual(delete == 0)

    def test_teacher(self):
        """teacher test"""
        teacher = Teacher.objects.create(
            reference_number="20001",
            last_name="jack01", age=28,
            email="jack@gmail.com",
            title="Piano Professor",
            nick_name="nick jack",
            special="Piano",
            password="1020120121")

        self.assertIsNotNone(teacher)

        rows = Teacher.objects.create(
            reference_number="20001",
            last_name="jack01", age=28,
            email="jack1111@gmail.com",
            title="Piano Professor",
            nick_name="nick jack",
            special="Piano",
            password="1020120121")

        self.assertNotEqual(rows == 0)  # add assertion here

        count = Student.objects.all().acount()
        self.assertNotEqual(count == 0)

        delete = Student.objects.all().first().delete()
        self.assertNotEqual(delete == 0)

    def test_Lesson(self):
        """lesson test"""
        lesson = Lesson.objects.create(
            name="piano lesson",
            lesson_num=5,
            lesson_price=200,
            interval=2,
            duration=2)

        self.assertIsNotNone(lesson)

        rows = Lesson.objects.create(
            name="piano lesson0001",
            lesson_num=6,
            lesson_price=200,
            interval=2,
            duration=2)

        self.assertNotEqual(rows == 0)  # add assertion here

        count = Lesson.objects.all().acount()
        self.assertNotEqual(count == 0)

        delete = Lesson.objects.all().first().delete()
        self.assertNotEqual(delete == 0)

    def test_lessonBook(self):
        """lessonbook test"""
        lessonbook = LessonBook.objects.create(
            lesson_id="100010",
            lesson_name="piano lesson",
            booking_time=datetime.datetime.now(),
            student_id="100020201")

        self.assertIsNotNone(lessonbook)

        rows = LessonBook.objects.create(
            lesson_id="100010",
            lesson_name="piano lesson",
            booking_time=datetime.datetime.now(),
            student_id="100020201")

        self.assertNotEqual(rows == 0)  # add assertion here

        count = LessonBook.objects.all().acount()
        self.assertNotEqual(count == 0)

        delete = LessonBook.objects.all().first().delete()
        self.assertNotEqual(delete == 0)


if __name__ == '__main__':
    unittest.main()
