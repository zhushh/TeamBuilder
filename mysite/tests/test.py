from django.test import TestCase, Client

from teamBuilder.models import *

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='peter', email='sptzxbbb@gmail.com')

    def test_user_created(self):
        c = Client()
        response = c.get('/api/', follow=True)
        print(response.status_code)
        print(response.redirect_chain)
