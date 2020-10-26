from django.contrib import admin
from .models import CustomerPost, CommodityPost
# Register your models here.

@admin.register(CustomerPost)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('CustomerName','CustomerPhone','CustomerAddress')
    list_per_page = 20
    # list_display_links = ('CustomerName')

@admin.register(CommodityPost)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('CommodityId','CommodityName','CommodityPrice','CommondityImage','CommodityNum')
    list_per_page = 20
    # list_display_links = ('CommodityId','CommodityName')