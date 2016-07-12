# from django.core.urlresolvers import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from rest_framework.request import Request
# from teamBuilder.models import *
# from mysite.serializers import UserSerializer



# class CreateUserTests(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('peter', 'sptzxbbb@gmail.com', 'teambuilder')
#         self.client.login(username='peter', password='teambuilder')
#         self.data = {'username': 'mike', 'password': 'zxczxczxc', 'email': 'mike@gmail.com'}

#     def test_create_user(self):
#         """
#         Ensure a new user object can be created.
#         """
#         url = reverse('user-list')
#         response = self.client.post(url, self.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class ReadUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('peter', 'sptzxbbb@gmail.com', 'teambuilder')
#         self.client.login(username='peter', password='teambuilder')
#         self.user = User.objects.create(username='john')

#     def test_can_read_user_list(self):
#         response = self.client.get(reverse('user-list'))
#         # response = self.client.get('/api/users/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_can_read_user_detail(self):
#         response = self.client.get(reverse('user-detail', args=[self.user.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class UpdateUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('peter', 'sptzxbbb@gmail.com', 'teambuilder')
#         self.client.login(username='peter', password='teambuilder')
#         self.user = User.objects.create(username='michael', first_name="Tyson")

#         self.data = UserSerializer(self.user, contet=context).data
#         self.data.update({'first_name': 'Changed'})

#     def test_can_update_user(self):
#         response = self.client.put(reverse('user-detail', args=[self.user.id]), self.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class DeleteUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = User.objects.create_superuser('peter', 'sptzxbbb@gmail.com', 'teambuilder')
#         self.client.login(username='peter', password='teambuilder')
#         self.user = User.objects.create(username='michael')

#     def test_can_delete_user(self):
#         response = self.client.delete(reverse('user-detail', args=[self.user.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

