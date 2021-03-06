from django.db import models
from TraverMsg.models import ScenicMsg
from TraverMsg.models import CityMsg

# Create your models here.
# 产品推荐展示模块


"""
# 1.供应商
"""


class Supplier(models.Model):
    # 创建合作等级类型
    type_choices = (
        ('1', '战略合作'),
        ('2', '广告代理'),
        ('3', '数据提供')
    )
    id = models.CharField('供应商id', max_length=100, primary_key=True)
    name = models.CharField('供应商名称', max_length=30)
    link_url = models.CharField('供应商网站链接', max_length=100)
    cooperation_type = models.CharField('合作类型', max_length=10, choices=type_choices, default='3')

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 2.产品信息
数据库当中用于选择的属性：起价、行程天数、出发城市、产品类型、景点、供应商、销量
"""


# 产品信息分为多个字段

class ProductMsg(models.Model):
    id = models.CharField('产品id', max_length=50, primary_key=True)
    name = models.CharField('产品名称', max_length=100)
    traver_days = models.CharField('行程天数', max_length=10)
    product_type = models.CharField('产品类型', max_length=50,null = True,blank = True)
    img_url = models.CharField('图片url', max_length=1000)
    supplier = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE)
    product_link = models.CharField('产品链接', max_length=1000)
    score = models.CharField('综合评分', max_length=10, null=True, blank=True)
    sell_num = models.CharField('产品销量', max_length=10, null=True, blank=True)
    comments_num = models.CharField('评论数', max_length=10)
    product_grade = models.CharField('产品等级', max_length=10)

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product_City(models.Model):
    product_id = models.CharField('产品id',max_length=100)
    city_id = models.CharField('供应城市', max_length=100)
    product_price = models.CharField('对应价格',max_length=10)

    class Meta:
        verbose_name = '产品供应表'
        verbose_name_plural = verbose_name
        unique_together = ('product_id', 'city_id')


class Product_Senic(models.Model):
    # 产品相关景点
    product_id = models.CharField('产品id', max_length=100)
    senic_name = models.CharField('景点名', max_length=100)

    class Meta:
        verbose_name = '产品景点表'
        verbose_name_plural = verbose_name

"""
# 3.门票信息
"""


class TicketsMsg(models.Model):
    id = models.CharField('门票id', max_length=20, primary_key=True)
    scenic_name = models.CharField('景点', max_length=50, null=True)
    ticket_content = models.CharField('门票描述', max_length=3000, null=True, blank=True)
    scense_address = models.CharField('场景地址', max_length=1000, null=True, blank=True)
    ticket_price = models.CharField('门票价格', max_length=10, null=True, blank=True)
    ticket_link = models.CharField('门票链接', max_length=1000)
    supplier_id = models.ForeignKey(Supplier, verbose_name='所属供应商', on_delete=models.CASCADE, null=True, blank=True)
    score = models.CharField('评分', max_length=10, null=True, blank=True)
    img_url = models.CharField('图片地址', max_length=1000, null=True, blank=True)
    city_name = models.CharField('所属城市', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '门票信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


"""
# 4.酒店信息
"""


class HotelMsg(models.Model):
    id = models.CharField('酒店id', max_length=100, primary_key=True)
    name = models.CharField('酒店名字', max_length=50)
    score = models.CharField('酒店评分', max_length=10, null=True, blank=True)
    hotel_price = models.CharField('酒店价格', max_length=10)
    hotel_content = models.CharField('酒店位置', max_length=300)
    img_url = models.CharField('图片url', max_length=1000, null=True, blank=True)
    supplier_id = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE, null=True, blank=True)
    hotel_link = models.CharField('酒店链接', max_length=1000)
    city_name = models.CharField('所属城市',max_length = 100,null=True,blank=True)
    sell_num = models.CharField('酒店人气', max_length=50)
    latest_time = models.CharField('最新情况', max_length=100)

    class Meta:
        verbose_name = '酒店信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


"""
# 5.攻略信息
"""


class StrategyMsg(models.Model):
    id = models.CharField('攻略id', max_length=20, primary_key=True)
    title = models.CharField('标题', max_length=100)
    link_url = models.CharField('攻略链接', max_length=1000)
    simple_content = models.CharField('简介', max_length=1000)
    supplier_id = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE, null=True, blank=True)
    img_url = models.CharField('图片链接', max_length=1000)
    scenic_name = models.CharField('相关景点', max_length=100)  # 允许为空

    class Meta:
        verbose_name = '攻略信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
