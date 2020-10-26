from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import CustomerPost

def customer_list(request):
    customer = CustomerPost.objects.all()
    context = {'customer': customer}
    return render(request,'customer/list.html',context)
