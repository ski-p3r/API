from rest_framework import serializers
from .models import Cart, CartItem
from shop.models import Product

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()  # Use a single product serializer, not many=True
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Use CartItemSerializer to serialize the related items
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

class CreateCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, data):
        product_id = data['product_id']
        quantity = data['quantity']

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError('Product does not exist.')

        if quantity <= 0:
            raise serializers.ValidationError('Quantity should be greater than zero.')

        if quantity > product.stock:
            raise serializers.ValidationError('Not enough stock available.')

        return data

    def save(self, **kwargs):
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        # Create a new cart if it doesn't exist
        cart, created = Cart.objects.get_or_create()

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.quantity += quantity
            if cart_item.quantity > Product.objects.get(pk=product_id).stock:
                raise serializers.ValidationError('Not enough stock available.')
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(cart=cart, product_id=product_id, quantity=quantity)

        return cart_item
