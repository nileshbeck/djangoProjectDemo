from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index, name='home'),

    path('', login, name='login'),

    path('register/', register, name='register'),

    path('add_products/', add_products, name='add_products'),

    path('delete_product/<int:pk>/', delete_product, name='delete_product'),

    path('update_product/<int:pk>/', update_product, name='update_product'),

    path('add_categories/', add_categories, name='add_categories'),

    path('add_customer/', add_customer, name='add_customer'),

    path('add_vender/', add_vender, name='add_vender'),

    path('customer_detail/', customer_detail, name='customer_detail'),

    path('update_customer/<int:pk>/', update_customer, name='update_customer'),
    
    path('delete_customer/<int:pk>/', delete_customer, name='delete_customer'),

    path('vender_detail/', vender_detail, name='vender_detail'),

    path('delete_vender/<int:pk>/', delete_vender, name='delete_vender'),

    path('order/', order, name='order'),
    
    path('product_list/', product_list, name='product_list'),




    # path('login/', login,name='login_view')


]
