from django.urls import path , include
from .views import(ProductListView , CategoryListView , ProductDetailView , CategoryDetailView ,
FileListView , FileDetailView
)

urlpatterns = [
        path('categories/' , CategoryListView.as_view() , name='category-list'),
        path('categories/<int:pk>/' , CategoryDetailView.as_view() , name='category -detail'),
        
        path('products/<int:product_pk>/files/' , CategoryListView.as_view() , name='category-list'),
        path('products/<int:product_pk>/files/<int:pk>/' , CategoryDetailView.as_view() , name='category -detail'),
        
        path('products/' , ProductListView.as_view() , name='product-list'),
        path('products/<int:pk>/' , ProductDetailView.as_view() , name='product-detail')
]