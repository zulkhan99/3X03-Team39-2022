from django.test import TestCase
from main.models import *

# Create your tests here.
class hospitalTestCase(TestCase):
    def setUp(self):
        Hospital.objects.create(name="Tan Tock Seng Hospital")
        Hospital.objects.create(name="National University Hospital")