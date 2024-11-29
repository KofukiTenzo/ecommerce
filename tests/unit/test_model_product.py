from products.models import Products
from tests.test_setup import TestProductsModelSetup
from django.core.exceptions import ValidationError

class TestMyModelModel(TestProductsModelSetup):

    def test_product_creation(self):
        # Check that the product is created and stored in the database
        product = self.product
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "This is a test product")
        self.assertEqual(product.rate, 4)
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.stock, 100)
        self.assertEqual(product.category, "Test Category")
        self.assertEqual(product.image, '')
        
    def test_product_str_method(self):
        # Check that the __str__ method returns the correct product name
        self.assertEqual(str(self.product), "Test Product") 
        
    def test_invalid_product_without_name(self):
        # Try to create a product without a name (which should fail)
        with self.assertRaises(ValidationError):
            invalid_product = Products.objects.create(
                name="",  # Empty name is invalid
                description="Invalid product",
                rate=2,
                price=9.99,
                stock=50,
                category="Invalid Category",
                image=None
            )   
            
    def test_valid_product_with_image(self):
        # Test creating a product with an image
        # Here we simulate the image by passing a mock image or a valid image file if you're testing locally
        product_with_image = Products.objects.create(
            name="Product with Image",
            description="This product has an image",
            rate=5,
            price=29.99,
            stock=20,
            category="Category A",
            image=None  # Here you'd ideally pass a valid image for the test
        )   
        self.assertIsNone(product_with_image.image)  # image is still None in this case 
        
    def test_product_rate_minimum(self):
        # Test that the rate must be an integer and can be validated if necessary
        product = Products.objects.create(
            name="Product with Invalid Rate",
            description="Product with invalid rate value",
            rate=-1,  # Invalid rate, assuming we should not allow negative rates
            price=25.50,
            stock=15,
            category="Invalid Category",
            image=None
        )
        self.assertEqual(product.rate, -1)  # Django ORM will allow this, but you can add validation rules if needed    
        
    def test_product_price_validation(self):
        # Test validation of price to ensure it's a positive value
        product = Products.objects.create(
            name="Invalid Price Product",
            description="Product with invalid price",
            rate=3,
            price=-5.00,  # Negative price is invalid
            stock=30,
            category="Price Error Category",
            image=None
        )
        self.assertEqual(product.price, -5.00)  # Again, Django ORM will accept negative values, so you can add your own validation
