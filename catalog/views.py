from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from catalog.models import Category
from .forms import CategoryForm, ProductForm
from .models import Product


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all().order_by('created_at')


@method_decorator(csrf_exempt, name='dispatch')
class CategoryReorderView(View):
    def post(self, request):
        print("🟢 AJAX ПОЛУЧЕН!")
        print("📥 Данные:", request.body)

        try:
            import json
            data = json.loads(request.body.decode('utf-8'))
            print("📋 Order:", data.get('order'))

            # Обновляем порядок только для активных категорий
            for new_order, category_id in enumerate(data['order'], 1):
                Category.objects.filter(id=category_id).update(order=new_order)

            print("💾 СОХРАНЕНО!")
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print("❌ ОШИБКА:", e)
            return JsonResponse({'status': 'error'}, status=400)


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
    success_url = reverse_lazy("catalog:products_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product
