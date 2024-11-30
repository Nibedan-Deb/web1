from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('shop/products/<int:id>/', views.products, name='products'),
    path('blog/', views.blog, name='blog'),
]