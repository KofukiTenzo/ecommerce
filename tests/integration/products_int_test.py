from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Products
from django.urls import reverse

class ProductApiTests(APITestCase):

    def setUp(self):
        # Set up some initial products in the database for testing
        self.product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'rate': 5,
            'price': 100.0,
            'stock': 10,
            'category': 'Test Category',
        }
        self.product = Products.objects.create(**self.product_data)
        self.url = reverse('products')  # Adjust to your actual API endpoint

    def test_view_products(self):
        # Test that all products are returned if no filters are applied
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # We have one product in setup

        # Test filtering products by name
        response = self.client.get(self.url, {'name': 'Test Product'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Filter should return 1 product

        # Test when no products are found
        response = self.client.get(self.url, {'name': 'Nonexistent Product'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_product(self):
        # Test adding a new product
        new_product_data = {
            'name': 'New Product',
            'description': 'Description of new product',
            'rate': 4,
            'price': 50.0,
            'stock': 20,
            'category': 'New Category'
        }

        response = self.client.post(reverse('add_product'), new_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'New Product')

        # Test adding a product that already exists
        response = self.client.post(reverse('add_product'), self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Should return an error

    def test_update_product(self):
        # Test updating an existing product
        updated_data = {
            'name': 'Updated Product',
            'description': 'Updated description',
            'rate': 5,
            'price': 120.0,
            'stock': 15,
            'category': 'Updated Category'
        }
        url = reverse('update_product', kwargs={'pk': self.product.pk})  # Path for updating product by ID

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Product')

        # Test updating a non-existent product
        url = reverse('update_product', kwargs={'pk': 999})  # Non-existent ID
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product(self):
        # Test deleting a product
        url = reverse('delete_product', kwargs={'pk': self.product.pk})  # Path for deleting product by ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        # Test deleting a non-existent product
        response = self.client.delete(reverse('delete_product', kwargs={'pk': 999}))  # Non-existent product
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
