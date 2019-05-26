from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sellers


class SellersList(ListView):
    model = Sellers

class SellersDetail(DetailView):
    model = Sellers


class SellersCreate(CreateView):
    model = Sellers
    template_name = "db/sellers_create.html"
    fields = ['seller_id', 'first_name', 'last_name', 'phone_number', 'id_code']
    success_url = reverse_lazy('seller_list')

class SellersUpdate(UpdateView):
    model = Sellers
    template_name = "db/sellers_update.html"
    fields = ['seller_id', 'first_name', 'last_name', 'phone_number', 'id_code']
    success_url = reverse_lazy('seller_list')

class SellersDelete(DeleteView):
    model = Sellers
    success_url = reverse_lazy('seller_list')
