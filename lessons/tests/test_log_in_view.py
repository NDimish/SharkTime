"""Tests of the log in view."""
from django.test import TestCase
from django.urls import reverse
from ..forms.loginforms import LogInForm
from ..models import User
# from .helpers import LogInTester
from django.contrib import messages

class LogInViewTestCase(TestCase):
    """Tests of the log in view."""

    def setUp(self):
        self.url = reverse('log_in')
        User.objects.create_user('johndoe@example.org',
        first_name = 'John',
        last_name = 'Doe',
        password = 'Password123',
        role='Student'
        )

    def test_log_in_url(self):
        self.assertEqual(self.url,'/lessons/student/log_in/')

    def test_get_log_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
        # messages_list = list(response.context['messages'])
        # self.assertEqual(len(messages_list), 0)

    def test_unsuccesful_log_in(self):
        form_input = {'username': 'johndoe@example.org', 'password': 'WrongPassword123'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())
        # messages_list = list(response.context['messages'])
        # self.assertEqual(len(messages_list), 1)
        # self.assertEqual(messages_list[0].level, messages.ERROR)

    def test_succesful_log_in(self):
        form_input = {'username': 'johndoe@example.org', 'password': 'Password123'}
        response = self.client.post(self.url, form_input,follow=True)
        self.assertTrue(self._is_logged_in())
        response_url = reverse('student_home')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'student_home.html')
        # messages_list = list(response.context['messages'])
        # self.assertEqual(len(messages_list), 0)

    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()

    # def test_valid_log_in_by_inactive_user(self):
    #     self.user.is_active = False
    #     self.user.save()
    #     form_input = {'email': 'janedoe@example.org', 'password': 'Password123'}
    #     response = self.client.post(self.url, form_input, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'student_home.html')
    #     form = response.context['form']
    #     self.assertTrue(isinstance(form, LogInForm))
    #     self.assertFalse(form.is_bound)
    #     self.assertFalse(self._is_logged_in())
    #     messages_list = list(response.context['messages'])
    #     self.assertEqual(len(messages_list), 1)
    #     self.assertEqual(messages_list[0].level, messages.ERROR)
