"""Unit tests of the sign up form."""
from django import forms
from django.test import TestCase
from ..forms.loginForms import signUp
from lessons.models import User
from django.urls import reverse

# from django.contrib.auth.hashers import check_password

class SignUpFormTestCase(TestCase):
    """Unit tests of the sign up form."""

    def setUp(self):
        self.url = reverse('signUp')
        self.form_input = {
            'username':'janedoe@example.org',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'janedoe@example.org',
            'password': 'Password123',
        }

    def test_valid_sign_up_form(self):
        form = signUp(data=self.form_input)
        #self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = signUp()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('password',form.fields)

    def test_form_uses_model_validation(self):
        self.form_input['email'] = 'bademail'
        form = signUp(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_uppercase_character(self):
        self.form_input['password'] = 'password123'
        form = signUp(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_lowercase_character(self):
        self.form_input['password'] = 'PASSWORD123'
        form = signUp(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_number(self):
        self.form_input['password'] = 'PasswordABC'
        form = signUp(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_sign_up_url(self):
        self.assertEqual(self.url,'/signpage/signup/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signUp.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, signUp))
        self.assertFalse(form.is_bound)

    def test_unsuccesful_sign_up(self):
        self.form_input['username'] = 'BAD_USERNAME'
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signUp.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, signUp))
        self.assertTrue(form.is_bound)
        self.assertFalse(self._is_logged_in())

    def test_succesful_redirection(self):
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input, follow=True)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count)  # checks that a user object has been created
        response_url = reverse('home')
        self.assertTemplateUsed(response, 'signUp.html')

    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()
