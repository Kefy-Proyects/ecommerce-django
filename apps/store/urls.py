from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.get_product, name='product'),
    path('category/<str:foo>', views.get_category, name='category'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('search/', views.search, name='search'),

]
