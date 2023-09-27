from django.test import TestCase
from django.urls import reverse
from shop.models import Product
from shop.views import ProductViewSet

class ProductViewSetTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product description.",
            price=19.99,
            stock=10,
        )

    def test_product_list_view(self):
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_product_detail_view(self):
        url = reverse("product-detail", args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    # Add more view tests as needed
