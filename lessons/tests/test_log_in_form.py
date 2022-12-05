"""Unit tests of the log in form."""
from django.test import TestCase
from django import forms
from ..forms.loginforms import LogInForm,SignUpForm

class LogInFormTestCase(TestCase):
    """Unit tests of the log in form."""


    def setUp(self):
        self.form_input = {'username': 'johndoe@domain.org', 'password': 'Password123'}

    def test_form_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        #email_field = form.fields['email']
        #self.assertTrue(isinstance(email_field.widget, forms.EmailInput))
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget, forms.PasswordInput))

    def test_form_accepts_valid_input(self):
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_rejects_blank_email(self):
        self.form_input['username'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_blank_password(self):
        self.form_input['password'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

# check this function
    def test_form_accepts_incorrect_email(self):
        self.form_input['username'] = 'ghl.com'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_accepts_incorrect_password(self):
        self.form_input['password'] = 'pwd'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())
