from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from catalog.models import Category
from .forms import CategoryForm
from .models import Product


class CategoryList(ListView):
    model = Category
    template_name = 'catalog/categories_list.html'


# def get_categories(request):
#     context = {
#         'categories': Category.objects.all(),
#     }
#
#     return render(request, 'catalog/categories_list.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    queryset = Product.objects.filter(is_active=True)
    extra_context = {'title': 'Каталог товаров'}


class ProductDetailView(DetailView):
    model = Product



# def get_product(request):
#     context = {
#         'products': Product.objects.all(),
#     }
#
#     return render(request, 'catalog/product_list.html', context)


# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.delete()
#         messages.success(request, 'Товар успешно удален.')
#         return redirect('catalog:get_product')
#
#     return render(request, 'catalog/confirm_delete_product.html', {
#         'product': product
#     })

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

# def create_category(request):
#     form = CategoryForm()

#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Категория успешно добавлена!")
#             return redirect('catalog:get_categories')
#
#     return render(request, 'catalog/category_form.html', {'form': form})
