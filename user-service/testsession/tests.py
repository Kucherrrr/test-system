from django.test import TestCase

class TestSessionViewTest(TestCase):
    def test_start_page(self):
        response = self.client.get('/start/')
        self.assertEqual(response.status_code, 200)