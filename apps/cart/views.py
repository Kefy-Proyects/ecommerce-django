from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from ..store.models import Product
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.

def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_products()
    quantities=cart.get_quantities()
    total=cart.get_total()
    return render(request, 'cart/cart_summary.html', {'cart_products':cart_products,'quantities':quantities, 'total':total})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action')== 'post':
        product_id = int(request.POST.get('product_id')) 
        product_qty = int(request.POST.get('product_qty')) 


        product = get_object_or_404(Product, id=product_id)
        if product.in_stock <= 0:
            messages.warning(request, 'There is no stock of this product.')
        else:
            cart.add(product=product, quantities=product_qty)
        cart_quantity = cart.__len__()

        #response=JsonResponse({'Product Name: ':product.name})
        response=JsonResponse({'qty':cart_quantity})


        return response

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action')== 'post':
        product_id = int(request.POST.get('product_id')) 

        cart.delete(product=product_id)

        response=JsonResponse({'id_deleted':product_id})

        return response

        return redirect('cart_summary')

def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action')== 'post':
        product_id = int(request.POST.get('product_id')) 
        product_qty = int(request.POST.get('product_qty')) 

        cart.update(product=product_id, quantities=product_qty)

        return redirect('cart_summary')
