from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    products=Product.objects.all()
    
    context={
        'products':products,
    }

    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html', {})

def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, ('Has accedido exitosamente!!!'))
            return redirect('home')
        else:
            messages.success(request, 'Ha ocurrido un inconveniente. Por favor, vuelva a intentar.')
            return redirect('login')
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):

    logout(request)
    messages.success(request, ('Ha salido de su cuenta.'))
    return redirect('home')