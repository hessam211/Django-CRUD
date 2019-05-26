from django.contrib import admin
from db.models import Customers, Products, Refs, Sellers, Selling, Sold, Transactions, Wallet, SellingEdits
admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Refs)
admin.site.register(Sold)
admin.site.register(Selling)
admin.site.register(Sellers)
admin.site.register(Transactions)
admin.site.register(Wallet)
admin.site.register(SellingEdits)


# Register your models here.
