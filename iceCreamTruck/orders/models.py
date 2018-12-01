import datetime

from django.db import models
from django.utils import timezone
from customers.models import Customer

class OrderForm(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,) 
    flavor = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    @property
    def total_cost(self):
        return '%s%s%s' % ('$', self.quantity * 50, '.00')
    
    @property
    def name(self):
        return '%s %s' % (self.customer.first_Name, self.customer.last_Name)
    @property
    def customer_i_d(self):
        return '%s' % (str(self.customer.customer_id).zfill(6),)

#货物信息表
class ProductForm(models.Model):
    #产品号我建议使用Char类型
    product_id=models.CharField(max_length=50)
    #单价
    price=models.FloatField(default=0.0)
    #剩余数量
    numbers=models.IntegerField(default=0)
    #产品名称
    pname=models.CharField(max_length=20)
    #产地
    parea=models.CharField(max_length=20)
