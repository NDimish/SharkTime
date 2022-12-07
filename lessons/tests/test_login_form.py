"""Unit tests of the log in form."""
from django.test import TestCase
from django import forms
from ..forms.loginForms import login

class LogInFormTestCase(TestCase):
    """Unit tests of the log in form."""


    def setUp(self):
        self.form_input = {'email': 'johndoe@domain.org', 'password': 'Password123'}

    def test_form_contains_required_fields(self):
        form = login()
        self.assertIn('email', form.fields)
        self.assertIn('password', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field.widget, forms.EmailInput))
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget, forms.PasswordInput))

    def test_form_accepts_valid_input(self):
        form = login(data=self.form_input)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_rejects_blank_email(self):
        self.form_input['email'] = ''
        form = login(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_blank_password(self):
        self.form_input['password'] = ''
        form = login(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_accepts_incorrect_email(self):
        self.form_input['email.'] = 'ghl.com'
        form = login(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_accepts_incorrect_password(self):
        self.form_input['password'] = 'pwd'
        form = login(data=self.form_input)
        self.assertTrue(form.is_valid())
