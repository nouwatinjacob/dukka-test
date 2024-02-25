from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import CustomUser

class AuthenticationTests(APITestCase):
    def test_registration(self):
        data = {'email': 'test_user@gmail.com', 'password': 'test_password',
                'confirm_password': 'test_password', 'country': 'NG',
                'full_name': 'Test  User', 'sex': 'male', 'phone_number': '+2348067846354'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'test_user@gmail.com')

    def test_login(self):
        user = CustomUser.objects.create_user(email='test_user@gmail.com', password='test_password')
        data = {'email': 'test_user@gmail.com', 'password': 'test_password'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_logout(self):
        user = CustomUser.objects.create_user(email='test_user@gmail.com', password='test_password')
        self.client.login(email='test_user@gmail.com', password='test_password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)