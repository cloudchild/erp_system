from django.urls import path
from . import views
app_name = 'sales'

urlpatterns = [
  path('customer-list/',views.customer_list,name= 'customer_list'),
]