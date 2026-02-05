from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from catalog.models import Category
from .forms import CategoryForm, ProductForm
from .models import Product


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("catalog:category_list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm


class CategoryDetailView(DetailView):
    model = Category


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:category_list")


class ProductUpdateView(UpdateView):
    model = Category
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product
