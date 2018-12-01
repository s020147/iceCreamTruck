import datetime

from django.db import models
from django.utils import timezone
from customers.models import Customer
from products.models import Product
from django.core.exceptions import ValidationError

class OrderForm(models.Model):
    order_i_d = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,) 
    flavor = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.quantity > self.flavor.quantity_stocked:
            raise ValidationError('Not enough product stocked.')
    
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
