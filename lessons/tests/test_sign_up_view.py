"""Tests of the sign up view."""
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from ..forms.loginforms import LogInForm,SignUpForm
from lessons.models import User

class SignUpViewTestCase(TestCase):
    """Tests of the sign up view."""

    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = { 'janedoe@example.org'
        'first_name': 'Jane',
        'last_name': 'Doe',
        'new_password': 'Password123',
        'password_confirmation': 'Password123',
        'role':'Student'
         }

    # def test_sign_up_url(self):
    #     self.assertEqual(self.url,'/sign_up/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)

    def test_unsuccesful_sign_up(self):
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)

    def test_succesful_sign_up(self):
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count)
        response_url = reverse('log_in')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'student_home.html')
        user=User.objects.get(username='janedoe@example.org')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.role, 'Student')
        is_password_correct = check_password('Password123',user.password)  # since the password will be hashed, so to check its equality dehash it using check_password
        self.assertTrue(is_password_correct)
        self.assertTrue(self._is_logged_in())

    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()
