from tokenize import Name
from webbrowser import get
from django.test import TestCase
from main.models import *

# Create your tests here.

#testing pytest
class hospitalTestCase(TestCase):
    def test_hospital_name(self):
        TTS = Hospital.objects.get(name="Tan Tock Seng Hospital")
        NUH = Hospital.objects.get(name="National University Hospital")
        self.assertEqual(TTS.name , "Tan Tock Seng Hospital")
        self.assertEqual(NUH.name , "National University Hospital")        