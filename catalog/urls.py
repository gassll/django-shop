from django.urls import path

from catalog import views
from catalog.views import CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, \
    CategoryDetailView

app_name = 'catalog'

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("products/", views.ProductCreateView.as_view(), name="get_product"),
    path('products/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path("categories/add", CategoryCreateView.as_view(), name="category_form"),
    path("categories/<int:pk>/delete", CategoryDeleteView.as_view(), name="category_delete"),
    path("categories/<int:pk>/update", CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/detail", CategoryDetailView.as_view(), name="category_detail"),
]
