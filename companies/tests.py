import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status


class TestCompanyListAPIView(TestCase):
    fixtures = ['company.yaml']

    def setUp(self):
        self.user = self.__create_user()
        self.token = self.__create_token()
        self.wrong_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.\
        eyJ1c2VyX2lkIjo0NjM1MiwiZW1haWwiOiJ5YW5zc3Nzc0BzdGFmZi5ncm\
        FtZWRpYS5jb20iLCJ1c2VybmFtZSI6InJ1bGx5QHN0YWZmLmdyYW1lZGlhL\
        mNvbSIsImV4cCI6MTUxODM1NDkwMSwib3JpZ19pYXQiOjE1MTgyNjg1MDF9.\
        qbYKpAJaluk25xL6NzhArKcB0arPT81-CucT8eHLqtU"

    def __create_user(self):
        return User.objects.create_user(
            username='mytest',
            email='mytest@mail.com',
            password='password1234')

    def __create_token(self):
        client = Client()
        payload = {
            'username': 'mytest',
            'password': 'password1234'
        }

        response = client.post('/token-auth/',
                               data=json.dumps(payload),
                               content_type='application/json')
        return json.loads(response.content).get('token')


    def test_get_company_success(self):
        response = Client().get('/companies/', HTTP_AUTHORIZATION=f'JWT {self.token}')

        expect = [
            {
                "name":"PT. Gramedia Digital Nusantara",
                "description":"Lorem ipsum dolor sit amet GDN"
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(expect, json.loads(response.content))

    def test_post_company_success(self):
        response = Client().post('/companies/',
                                 data=json.dumps({
                                     'name': 'PT. Gramedia Asri Media',
                                     'description': 'Lorem Ipsum'
                                 }),
                                 HTTP_AUTHORIZATION=f'JWT {self.token}',
                                 content_type='application/json')
        expect = {
            'name': 'PT. Gramedia Asri Media',
            'description': 'Lorem Ipsum'
         }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(expect, json.loads(response.content))

    def test_get_company_fail(self):
        response = Client().get('/companies/', HTTP_AUTHORIZATION=f'JWT {self.wrong_token}')

        expect = {
            "detail":"Invalid Authorization header. Credentials string should not contain spaces."
        }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertDictEqual(expect, json.loads(response.content))

    def test_post_company_fail(self):
        response = Client().post('/companies/',
                                 data=json.dumps({
                                     'name': 'PT. Gramedia Asri Media',
                                     'description': 'Lorem Ipsum'
                                 }),
                                 HTTP_AUTHORIZATION=f'JWT {self.wrong_token}',
                                 content_type='application/json')
        expect = {
            "detail":"Invalid Authorization header. Credentials string should not contain spaces."
        }

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertDictEqual(expect, json.loads(response.content))
