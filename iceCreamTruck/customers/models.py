from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):   
    customer_id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length = 25)
    last_Name = models.CharField(max_length = 25)
    street_Address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 2, validators=[RegexValidator('.{2}$')])
    zip_Code = models.CharField(max_length = 5, validators=[RegexValidator('^\d{5}$')])
    
    def __str__(self):
        return '%s %s %s' % (str(self.customer_id).zfill(6), self.first_Name, self.last_Name)
