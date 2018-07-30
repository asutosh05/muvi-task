from django.test import TestCase
from .models import Content
# Create your tests here.

Class ContentTestCase(TestCase):
    
    def test_Create_Content(self):
        Content.objects.create(owner=1,name="Django video",releaseDate='07/30/2018')
