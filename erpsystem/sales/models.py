from django.db import models

# Create your models here.
# 导入内建的user模型
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务
from django.utils import timezone

# 销售管理数据模型
# 客户
class CustomerPost(models.Model):
    '''
        客户管理：客户名、联系电话、地址
    '''
    # 客户名。models.CharField 为字符串字段，
    CustomerName = models.CharField('客户名',max_length=20)
    # 客户电话
    CustomerPhone = models.CharField('联系电话',max_length=11,blank=True,null=True)
    # 客户地址
    CustomerAddress = models.CharField('地址',max_length=50)
    #创建时间
    CustomerCreated = models.DateTimeField(default=timezone.now)
    CustomerUpdated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户信息'
        ordering = ('-CustomerCreated',)
    def __str__(self):
        # 讲客户名称返回
        return self.CustomerName

# 产品
class CommodityPost(models.Model):
    '''
        产品信息：编号，名称，数量 价格，图片
    '''
    CommodityName = models.CharField('商品名称', max_length=100)
    CommodityId = models.CharField('商品编号', max_length=50,blank = True)
    CommodityPrice = models.DecimalField('商品价格', max_digits=11,decimal_places = 2)
    CommondityImage = models.ImageField('商品图片', upload_to='commondity_img/%Y%m%d/', blank=True, null=True)
    CommodityDateTime = models.DateTimeField('登记日期', auto_now_add=True)
    CommodityNum = models.DecimalField('商品数量',max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品信息'
        # 按时间下降排序
        ordering = ['-CommodityDateTime']

    def __str__(self):
        return self.CommodityName

# 订单
# class OrderPost(models.Model):
#     '''
#         产品信息：编号，名称，数量 价格，图片
#     '''
#
#     OrderId = models.CharField('订单编号', max_length=50,blank = True)
#     OrderCreated = models.DateTimeField('登记日期', auto_now_add=True)
#     OrderName = models.CharField('商品名称', max_length=100)
#     CommodityPrice = models.DecimalField('商品价格', max_digits=11,decimal_places = 2)
#     OrderNum = models.ImageField('商品数量', upload_to='commondity_img/%Y%m%d/', blank=True, null=True)
#     OrderPrice = models.CharField('总价')
#     ordstatus = models.('订单状态',max_digits=10, decimal_places=0)
#
#     class Meta:
#         verbose_name = '订单'
#         verbose_name_plural = '订单信息'
#         # 按时间下降排序
#         ordering = ['-CommodityDateTime']
#
#     def __str__(self):
#         return self.CommodityName