from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

# self.assertEqual(some_object_you_test, False/True)


class LinksShowTests(TestCase):
    def no_links_yet(self):
        response = self.client.get(reverse('favlinks:favlinks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
        self.assertQuerysetEqual(response.context['links'], [])