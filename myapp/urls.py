from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(),
         name='product_detail'),
    path('products/add/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/update/<int:pk>',
         views.ProductUpdatView.as_view(), name='update_product'),
    path('products/delete/<int:pk>',
         views.ProductDeleteView.as_view(), name='delete_product'),
    path('products/mylistings', views.my_listings, name='mylistings'),
]
