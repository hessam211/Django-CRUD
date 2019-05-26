# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(blank=True, null=True)
    wallet = models.ForeignKey('Wallet', models.DO_NOTHING, blank=True, null=True)
    ref = models.ForeignKey('Refs', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customers'




class Products(models.Model):
    product_id = models.CharField(primary_key=True, max_length=15)
    product_name = models.CharField(max_length=20)
    seller = models.ForeignKey('Sellers', models.DO_NOTHING, blank=True, null=True)
    product_specs = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Products'


class Refs(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Refs'


class Sellers(models.Model):
    seller_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sellers'


class Selling(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=15)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Selling'


class SellingEdits(models.Model):
    sale_id = models.CharField(max_length=15, blank=True, null=True)
    product_id = models.CharField(max_length=15, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Selling_edits'


class Sold(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    time_sold = models.TimeField(blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sold'


class Transactions(models.Model):
    sale = models.ForeignKey(Selling, models.DO_NOTHING, blank=True, null=True)
    transaction_id = models.CharField(primary_key=True, max_length=15)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    price_payed = models.FloatField(blank=True, null=True)
    time_sold = models.TimeField(blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Transactions'


class Wallet(models.Model):
    wallet_id = models.CharField(primary_key=True, max_length=10)
    wallet_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Wallet'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
