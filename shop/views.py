from django_filters.rest_framework import CharFilter, DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, CreateProductSerializer, GetCategorySerializer, ProductSerializer

class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']

class PageForCategory(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.select_related('parent').filter(parent=None)
    pagination_class = PageForCategory
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)  # Should be ('name',)

    def get_serializer_class(self):
        if self.action == 'create':
            return CategorySerializer
        elif self.action == 'list' or self.action == 'retrieve':
            return GetCategorySerializer
        return CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = PageForCategory
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['name', 'description']
    filterset_class = ProductFilter
    permission_classes = [IsAdminUser|ReadOnly]

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_serializer_class(self):
        # if self.request.user.is_staff:
        if self.action == 'create':
                return CreateProductSerializer
        return ProductSerializer
