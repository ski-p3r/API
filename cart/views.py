from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cart
from .serializers import CartSerializer, CartItemSerializer, CreateCartSerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCartSerializer  # Rename CreateCartSerializer to CreateCartItemSerializer
        return CartSerializer
