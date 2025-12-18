from django.test import TestCase
from .ai import classify_text

# Create your tests here.
class AITest(TestCase):
    def test_technology_classification(self):
        text = "AI and cloud automation software"
        self.assertEqual(classify_text(text), "Technology")

        