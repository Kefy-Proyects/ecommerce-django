from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, UserUpdateForm
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Product,Category
# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'store/profile.html',{})
    else:
        messages.warning('You most be loged!!')
        return redirect('home')

def update_profile(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=UserUpdateForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'User has been updated!!!')
            return render('home')
        else:
            print('su')
            messages.error(request, 'Something goes wrong')
            return render(request, 'store/update_profile.html', {'user_form':user_form})
    else:
        messages.warning('You must be logged in!!')
        return redirect('home')

def change_password(request):
    pass

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