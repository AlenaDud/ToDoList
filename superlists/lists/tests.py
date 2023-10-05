from django.test import TestCase
from django.urls import resolve
from lists.views import HomePageView
from django.http import HttpRequest


class HomePageTest(TestCase):
    """Testing Home Page."""

    def test_root_url_resolves_to_home_page_view(self):
        """Test: root URL resolving to view of home_page."""
        found = resolve('/')
        self.assertEqual(found.func, HomePageView.as_view())

    def test_home_page_returns_correct_html(self):
        """Test: home page return correct html."""
        request = HttpRequest()
        response = HomePageView.get(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', html)
        self.assertTrue(html.endswith('<html>'))
