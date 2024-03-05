from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestUserManagement(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_url = reverse('user_detail')
        self.user_data = {
            'email': 'test@example.com', 'password': 'test_password',
            'confirm_password': 'test_password', 'country': 'NG',
            'full_name': 'Test  User', 'sex': 'male',
            'phone_number': '+2348067846354'
        }
        self.login_data = {
            'email': 'test@example.com',
            'password': 'test_password'
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(self.login_url, self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)

    def test_logout_user(self):
        self.client.post(self.register_url, self.user_data, format='json')
        login_response = self.client.post(self.login_url, self.login_data, format='json')
        refresh_token = login_response.data['refresh_token']
        response = self.client.post(self.logout_url, {"refresh_token": refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        self.client.post(self.register_url, self.user_data, format='json')
        login_response = self.client.post(self.login_url, self.login_data, format='json')
        access_token = login_response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['email'], self.user_data['email'])
        