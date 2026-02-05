from django.urls import path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path("categories/", views.ProductListView.as_view(), name="get_categories"),
    path("products/", views.ProductCreateView.as_view(), name="get_product"),
    path('products/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path("categories/add", views.ProductCreateView.as_view(), name="category_form"),
]
