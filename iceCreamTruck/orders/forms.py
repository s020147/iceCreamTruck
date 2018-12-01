from django import forms
from orders.models import OrderForm

class OrderModelForm(forms.ModelForm):

    class Meta:
        model = OrderForm
        fields = '__all__'
        exclude=('current_date',)

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductForm
        fields = '__all__'
