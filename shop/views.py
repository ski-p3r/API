from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Category, Product
from .serializers import CategorySerializer, GetCategorySerializer, ProductSerializer

class PageForCategory(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.select_related('parent').filter(parent=None)
    pagination_class = PageForCategory 

    def get_serializer_class(self):
        if self.action == 'create':
            return CategorySerializer
        elif self.action == 'list' or self.action == 'retrieve':
            return GetCategorySerializer
        return CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
