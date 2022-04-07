from django.test import TestCase, Client
from django.urls import reverse, resolve
from web.views import *


class TestUrls(TestCase):

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_result_url(self):
        path = reverse('result')
        assert resolve(path).view_name == 'result'


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view_get(self):
        req = self.client.get(reverse('home'))

        assert req.status_code == 200
        self.assertContains(req, 'BMI Calculator')\

    def test_result_view_post(self):
        req = self.client.post(reverse('result'), data={
            'feet': 6,
            'inches': 6,
            'weight': 143
        })

        self.assertContains(req, 'Result BMI: 16.9, Underweight')
    

