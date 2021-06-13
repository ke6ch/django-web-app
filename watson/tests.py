from django.test import TestCase
from django.urls import reverse
from django.urls import resolve


class TestUrls(TestCase):
    def test_chat_url(self):
        path = reverse("chat")
        assert resolve(path).view_name == "chat"
