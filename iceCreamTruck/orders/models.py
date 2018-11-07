import datetime

from django.db import models
from django.utils import timezone


class OrderForm(models.Model):
    question_text = models.CharField(max_length=200)
    product_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total_cost= models.IntegerField(default=0)
    current_date = models.DateTimeField('current date')
    def __str__(self):
        return self.id
    def was_ordered_recently(self):
        return self.current_date >= timezone.now()-datetime.timedelta
    

class Choice(models.Model):
    question = models.ForeignKey(OrderForm,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
