import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items()  # Corrected method call
    else:
        items = []
        cart_items = 0  # Default value for non-authenticated users

    context = {'items': items, 'cart_items': cart_items}  # Corrected key name 'cartItems'
    products = Product.objects.all()
    context['products'] = products  # Add products to context
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items()  # Corrected method call
    else:
        items = []
        cart_items = 0  # Default value for non-authenticated users

    context = {'items': items, 'order': order, 'cartItems': cart_items}  # Corrected key name 'cartItems'
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items()  # Corrected method call and variable name
    else:
        items = []
        cart_items = 0  # Default value for non-authenticated users

    context = {'items': items, 'order': order, 'cart_items': cart_items}  # Corrected key name 'cartItems'
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', product_id)
    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was updated', safe=False)
