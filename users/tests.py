import http
import json

from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestTokenAuth(TestCase):

    def setUp(self):
        pass

    def __create_user(self):
        return User.objects.create_user(
            username='johndoe',
            email='johndoe@gmail.com',
            password='password1234')

    def test_login_success(self):
        self.__create_user()

        client = Client()
        response = client.post('/token-auth/', data=json.dumps({
            'username': 'johndoe',
            'password': 'password1234'
        }), content_type='application/json')

        self.assertEquals(response.status_code, int(http.HTTPStatus.OK))
        self.assertIsNotNone(json.loads(response.content).get('token'))

    def test_login_fail(self):
        self.__create_user()

        client = Client()
        response = client.post('/token-auth/', data=json.dumps({
            'username': 'johndoes',
            'password': 'password1234'
        }), content_type='application/json')

        self.assertEquals(response.status_code, int(http.HTTPStatus.BAD_REQUEST))
        self.assertIsNone(json.loads(response.content).get('token'))