"""Tests of the log in view."""
from django.test import TestCase
from django.urls import reverse
from ..forms.loginForms import login
from ..models import User

class LogInViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('login')
        User.objects.create_user('johndoe@example.org',
         first_name='John',
         last_name='Doe',
         role='S',
         password='Password123',
        )

    def test_log_in_url(self):
        self.assertEqual(self.url,'/signpage/login/')

    def test_get_log_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, login))

    #tests that the login is unsuccesful for wrong passwords
    def test_unsuccesful_log_in(self):
        form_input = {'username': 'johndoe@example.org', 'password': 'WrongPassword123'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, login))
        self.assertFalse(self._is_logged_in())

    #tests that the login is succesful for a correct passwords
    def test_succesful_log_in(self):
        form_input = {'username': 'johndoe@example.org', 'password': 'Password123'}
        response = self.client.post(self.url, form_input,follow=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()
