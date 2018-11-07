from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import OrderForm

def index(request):
    latest_order_list = OrderForm.objects.order_by('-current_date')[:5]
    context = {'latest_order_list':latest_order_list}
    return render(request,'orders/index.html',context)
def detail(request, order_id):
    order = get_object_or_404(OrderForm, pk=order_id)
    return render(request,'orders/detail.html',{'order':order})
def results(request, order_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % order_id)

def vote(request, order_id):
    return HttpResponse("You're voting on question %s." % order_id)
