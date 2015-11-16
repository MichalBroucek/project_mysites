from django.test import TestCase
from django.utils import timezone

from news.models import New
from news.models import PhotoOfWeek



# Create your tests here. ##################################################

class NewMethodTests(TestCase):

    def test_new_get_unicode(self):
        """
        Test unicode function of New class from model
        """
	new = New(title="Novinka", date=timezone.now(), text="Text novinky")
        self.assertEqual(new.__unicode__(), "Novinka")


class PhotoOfWeekMethodTests(TestCase):

    def test_photoofweek_get_unicode(self):
        """
        Test unicode function of PhotoOfWeek class from model
        """
	photoOfWeek = PhotoOfWeek(title="Photo of week", text="Text of photo of week")
        self.assertEqual(photoOfWeek.__unicode__(), "Photo of week")

