import xadmin
from .models import ProductMsg
from .models import Supplier
from .models import TicketsMsg
from .models import HotelMsg
from .models import StrategyMsg
from .models import Product_City
from .models import Product_Senic


# Register your models here.
# xadmin中这里是继承object，不再是继承admin
class ProductMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'traver_days',
                    'product_type', 'supplier',
                    'product_link', 'score', 'sell_num']
    # 搜索的字段
    search_fields = ['id','name', 'product_type']
    # 过滤
    list_filter = ['id', 'name', 'supplier',
                   'product_link', 'score', 'sell_num']


class ProductCityAdmin(object):
    # 显示的列
    list_display = ['product_id', 'city_id', 'product_price']
    # 搜索的字段
    search_fields = ['city_id','product_id']
    # 过滤
    list_filter = ['product_id', 'city_id', 'product_price']


class ProductScenicAdmin(object):
    # 显示的列
    list_display = ['product_id', 'senic_name']
    # 搜索的字段
    search_fields = ['senic_name','product_id']
    # 过滤
    list_filter = ['product_id', 'senic_name']


class SupplierAdmin(object):
    # 显示的列
    list_display = ['id', 'name', 'link_url', 'cooperation_type']
    # 搜索的字段
    search_fields = ['name', 'cooperation_type']
    # 过滤
    list_filter = ['id', 'name', 'link_url', 'cooperation_type']


class TicketMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'scenic_name', 'city_name', 'img_url', 'score','ticket_link', 'scense_address',
                    'ticket_price']
    # 搜索的字段
    search_fields = ['id','scenic_name','city_name']
    # 过滤
    list_filter = ['id', 'scenic_name','city_name', 'ticket_content', 'ticket_price']


class HotelMsgAdmin(object):
    # 显示的列
    list_display = ['name', 'score', 'hotel_price',  'img_url','hotel_link',
                    'hotel_content', 'city_name', 'supplier_id' ]
    # 搜索的字段
    search_fields = ['name','hotel_content', 'city_name']
    # 过滤
    list_filter = ['id', 'name', 'score', 'hotel_price','city_name',
                   'img_url', 'supplier_id', 'hotel_link']


class StrategyMsgAdmin(object):
    # 显示的列
    list_display = ['id', 'title', 'link_url', 'simple_content', 'supplier_id', 'img_url',  'scenic_name']
    # 搜索的字段
    search_fields = ['title', 'link_url']
    # 过滤
    list_filter = ['id', 'title', 'link_url', 'simple_content', 'supplier_id', 'img_url', 'scenic_name']


# 将基本配置管理与view绑定
xadmin.site.register(Supplier, SupplierAdmin)
xadmin.site.register(ProductMsg, ProductMsgAdmin)
xadmin.site.register(TicketsMsg, TicketMsgAdmin)
xadmin.site.register(HotelMsg, HotelMsgAdmin)
xadmin.site.register(StrategyMsg, StrategyMsgAdmin)
xadmin.site.register(Product_Senic, ProductScenicAdmin)
xadmin.site.register(Product_City, ProductCityAdmin)
