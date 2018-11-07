from django import forms
from orders.models import OrderForm

class OrderModelForm(forms.ModelForm):

    class Meta:
        model = OrderForm
        fields = '__all__'
