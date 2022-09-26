from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('家用机器人', '家用机器人'),
        ('智能监控', '智能监控'),
        ('人脸识别解决方案', '人脸识别解决方案'),
    )
    title = models.CharField(max_length=50, verbose_name=' 产品标题')
    description = models.TextField(verbose_name='产品详情描述')
    productType = models.CharField( choices=PRODUCTS_CHOICES,
                                    max_length=50,
                                    verbose_name='产品类型'
                                    )
    price = models.DecimalField(max_digits=7,
                                decimal_places=1,
                                null=True,
                                verbose_name='产品价格'
                                )