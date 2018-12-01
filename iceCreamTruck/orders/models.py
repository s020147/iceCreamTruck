import datetime

from django.db import models
from django.utils import timezone
from customers.models import Customer
from products.models import Product

class OrderForm(models.Model):
    order_i_d = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,) 
    flavor = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    @property
    def _product_id(self):
        return '%s' % (str(self.flavor.flavor_i_d).zfill(6),)
        
    @property
    def total_cost(self):
        return '$%s' % (self.quantity * self.flavor.price)
    
    @property
    def name(self):
        return '%s %s' % (self.customer.first_Name, self.customer.last_Name)
        
    @property
    def _customer_id(self):
        return '%s' % (str(self.customer.customer_i_d).zfill(6),)

    @property
    def _order_id(self):
        return '%s' % (str(self.order_i_d).zfill(6),)
