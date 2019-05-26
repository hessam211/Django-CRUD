from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # [...]
    path('seller', views.SellersList.as_view(), name='seller_list'),
    path('seller/<int:pk>', views.SellersDetail.as_view(), name='seller_detail'),
    path('create', views.SellersCreate.as_view(), name='seller_create'),
    path('update/<int:pk>', views.SellersUpdate.as_view(), name='seller_update'),
    path('delete/<int:pk>', views.SellersDelete.as_view(), name='seller_delete'),
]