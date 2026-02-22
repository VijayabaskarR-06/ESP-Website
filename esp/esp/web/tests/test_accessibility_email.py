from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse


class AccessibilityEmailTests(TestCase):

    @patch('esp.web.views.main.Tag.getBooleanTag')
    def test_contact_page_email_is_text(self, mock_get_tag):
        mock_get_tag.return_value = True
        response = self.client.get('/contact/contact/')
        self.assertContains(response, 'info@learningu.org')
        self.assertContains(response, 'mailto:info@learningu.org')
        self.assertNotContains(response, '<img src="')

    def test_privacy_page_email_is_text(self):
        response = self.client.get(reverse('privacy'))
        self.assertContains(response, 'info@learningu.org')
        self.assertContains(response, 'mailto:info@learningu.org')
        self.assertNotContains(response, '<img src="')
