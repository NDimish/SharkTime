from lessons.models import LessonRequest as request
from django.test import TestCase
from django import forms
from ..forms.adminForms import bookingForm
from django.urls import reverse


class AdminTestCase(TestCase):
    """Unit tests of the admin form."""

    def setUp(self):
        self.url = reverse('home')
        self.form_input = {'request':'no' , 'lesson_time':'30', 'lesson_type':'class',
        'lesson_teacher':'john','lesson_start_date':'2022-12-07','lesson_duration':'30',
        'lesson_interval':'1 lesson every week','lesson_day_of_week':'1'}

    def test_form_contains_required_fields(self):
        form = bookingForm()
        self.assertIn('lesson_time', form.fields)
        self.assertIn('lesson_type', form.fields)
        self.assertIn('lesson_teacher', form.fields)
        self.assertIn('lesson_start_date', form.fields)
        self.assertIn('lesson_duration', form.fields)
        self.assertIn('lesson_interval', form.fields)
        self.assertIn('number_of_lessons', form.fields)
        self.assertIn('lesson_day_of_week', form.fields)
        lesson_time_field = form.fields['lesson_time']
        self.assertTrue(isinstance(lesson_time_field.widget, forms.TimeInput))
        lesson_type_field = form.fields['lesson_type']
        self.assertTrue(isinstance(lesson_type_field.widget, forms.TextInput))
        lesson_teacher_field = form.fields['lesson_teacher']
        self.assertTrue(isinstance(lesson_teacher_field.widget, forms.TextInput))
        number_of_lessons_field=form.fields['number_of_lessons']
        self.assertTrue(isinstance(number_of_lessons_field.widget,forms.NumberInput))
        lesson_day_of_week_field = form.fields['lesson_day_of_week']
        self.assertTrue(isinstance(lesson_day_of_week_field.widget, forms.Select))

    def test_form_rejects_blank_fields(self):
        self.form_input['lesson_teacher'] = ''
        form = bookingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.form_input['lesson_type'] = ''
        form = bookingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.form_input['lesson_time'] = ''
        form = bookingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.form_input['number_of_lessons'] = ''
        form = bookingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.form_input['lesson_day_of_week'] = ''
        form = bookingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
