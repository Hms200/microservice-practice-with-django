from django.test import TestCase
from .models import Order, Shop


class ShopModelTest(TestCase):
    def test_sample(self):
        temp = True
        self.assertIs(temp, True)