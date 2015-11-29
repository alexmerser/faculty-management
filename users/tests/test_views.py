from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from users.models import Staff


class TestStaffDetail(TestCase):
    def test_single(self):
        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        response = self.client.get(reverse('staff_detail', args=(staff.pk,)))
        self.assertContains(response, staff.name)
        self.assertEqual(response.status_code, 200)
