# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import View, TemplateView
# from django.contrib import messages
# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from django.utils.decorators import method_decorator
# from catalog.models import Product
# from .cart import Cart
#
#
# class CartSummaryView(TemplateView):
#     """Отображение корзины"""
#
#     template_name = 'cart/cart.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cart = Cart(self.request)
#         context['cart'] = cart
#         context['total_price'] = cart.get_total_price()
#         return context
#
#
# class CartAddView(View):
#     """Добавление товара в корзину"""
#
#
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         cart = Cart(request)
#
#         quantity = int(request.POST.get('quantity', 1))
#         update_quantity = request.POST.get('update_quantity') == 'true'
#
#         cart.add(product, quantity, update_quantity)
#
#         messages.success(request, f'{product.name} добавлен в корзину')
#
#         if 'next' in request.POST:
#             return redirect(request.POST['next'])
#         return redirect('cart:cart_summary')
#
#
# class CartUpdateView(View):
#     """Обновление количества товара в корзине"""
#
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         cart = Cart(request)
#         quantity = int(request.POST.get('quantity', 0))
#
#         if quantity > 0:
#             cart.add(product, quantity, update_quantity=True)
#         else:
#             cart.remove(product)
#
#         return JsonResponse({
#             'total_items': len(cart),
#             'total_price': str(cart.get_total_price())
#         })
#
#
# class CartRemoveView(View):
#     """Удаление товара из корзины"""
#
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#         cart = Cart(request)
#         cart.remove(product)
#
#         return JsonResponse({
#             'total_items': len(cart),
#             'total_price': str(cart.get_total_price())
#         })
#
#
# class CartClearView(View):
#     """Очистка корзины"""
#
#     def post(self, request):
#         cart = Cart(request)
#         cart.clear()
#         messages.success(request, 'Корзина очищена')
#         return JsonResponse({'message': 'Корзина очищена'})
#
#
# @method_decorator(require_http_methods(["GET"]), name='dispatch')
# class CartDetailAjaxView(View):
#     """AJAX представление для получения данных корзины"""
#
#     def get(self, request):
#         cart = Cart(request)
#         items = list(cart)
#
#         return JsonResponse({
#             'items': [{
#                 'id': item['product'].id,
#                 'name': str(item['product']),
#                 'price': str(item['price']),
#                 'quantity': item['quantity'],
#                 'total_price': str(item['total_price'])
#             } for item in items],
#             'total_items': len(cart),
#             'total_price': str(cart.get_total_price())
#         })
