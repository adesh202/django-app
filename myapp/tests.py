from django.test import TestCase

class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Jenkins CI/CD!")
