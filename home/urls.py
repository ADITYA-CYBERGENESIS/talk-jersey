from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('createaccount/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
    path('product/', views.product, name='product'),
    path('shop/', views.shop, name='shop'),
]
