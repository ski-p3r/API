from django.test import TestCase
from shop.models import Product

class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product description.",
            price=19.99,
            stock=10,
        )

    def test_product_name(self):
        self.assertEqual(self.product.name, "Test Product")

    def test_product_description(self):
        self.assertEqual(self.product.description, "This is a test product description.")

    def test_product_price(self):
        self.assertEqual(self.product.price, 19.99)

    def test_product_stock(self):
        self.assertEqual(self.product.stock, 10)

    # Add more model tests as needed
