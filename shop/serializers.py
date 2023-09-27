from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']

class RecursiveCategorySerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data

class GetCategorySerializer(serializers.ModelSerializer):
    child = RecursiveCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'child']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        children = instance.child.all()
        
        if not children:
            data.pop('child')
        
        return data


class ProductSerializer(serializers.ModelSerializer):
    category = GetCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']
