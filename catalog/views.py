from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from catalog.models import Category
from .forms import CategoryForm
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
    template_name = 'catalog/product_list.html'
    queryset = Product.objects.filter(is_active=True)
    extra_context = {'title': 'Каталог товаров'}


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')


class ProductCreateView(CreateView):
    model = Product
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Категория успешно добавлена!")
        return response
