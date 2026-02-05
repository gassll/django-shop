from django.urls import path

from catalog import views
from catalog.views import CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, \
    CategoryDetailView, ProductListView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/add", CategoryCreateView.as_view(), name="category_form"),
    path("categories/<int:pk>/delete", CategoryDeleteView.as_view(), name="category_delete"),
    path("categories/<int:pk>/update", CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/detail", CategoryDetailView.as_view(), name="category_detail"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/add", ProductCreateView.as_view(), name="product_form"),
]
