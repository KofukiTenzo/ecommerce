from django.test import TestCase
from rest_framework.test import APIClient

from products.models import Products

class TestProductsModelSetup(TestCase):
    
    def setUp(self):
        # Create a valid product instance for testing
        self.product = Products.objects.create(
            name="Test Product",
            description="This is a test product",
            rate=4,
            price=19.99,
            stock=100,
            category="Test Category",
            image=None  # Since image is optional, it's set to None here
        )