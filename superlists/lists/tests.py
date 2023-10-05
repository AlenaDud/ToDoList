from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve, reverse
from lists.views import HomePageView
from django.http import HttpRequest


class HomePageTest(TestCase):
    """Testing Home Page."""
    def setUp(self) -> None:
        self.url = reverse('home')

    def test_home_page_returns_correct_html(self):
        """Test: home page is using correct view and template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'lists/home.html')
