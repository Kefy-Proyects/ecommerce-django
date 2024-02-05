from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Product,Category
# Create your views here.

def get_category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category=Category.objects.get(name=foo)
        
        products=Product.objects.filter(category=category)
        return render(request, 'store/category.html', {'products':products,'category':category})
    except:
        messages.error(request, 'That category does not exist.')
        return redirect('home')

    

def get_product(request, pk):
    product=get_object_or_404(Product,pk=pk)

    return render(request, 'store/product.html', {'product':product})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']

            user=authenticate(username=username, password=password)
            
            login(request, user)

            messages.success(request, (f'Bienvenido, {username}!!!'))
            return redirect('home')
    else:
        form = SignUpForm()
        
    return render(request, 'store/register.html', {'form':form})

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
            
            messages.error(request, 'Ha ocurrido un inconveniente. Por favor, vuelva a intentar.')
            return redirect('login')
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):

    logout(request)
    messages.info(request, ('Ha salido de su cuenta.'))
    return redirect('home')