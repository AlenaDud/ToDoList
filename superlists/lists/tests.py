from django.test import TestCase
from django.urls import resolve, reverse
from lists.views import HomePageView
from django.http import HttpRequest


class HomePageTest(TestCase):
    """Testing Home Page."""
    def setUp(self) -> None:
        self.url = reverse('home')

    def test_root_url_resolves_to_home_page_view(self):
        """Test: root URL resolving to view of home_page."""
        request = HttpRequest()
        request.method = 'GET'
        request.path = '/'
        resolver = resolve(request.path)
        self.assertEqual(resolver.func.view_class, HomePageView)

    def test_home_page_returns_correct_html(self):
        """Test: home page return correct html."""
        response = self.client.get(self.url)
        html = response.content.decode()
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
