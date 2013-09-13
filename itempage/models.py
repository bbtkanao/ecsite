# coding: utf-8
from django.db import models

class AbstractItem(models.Model):
    item_name = models.CharField(u"商品名", max_length=256)
    price = models.PositiveIntegerField(u"価格")

    def __unicode__(self):
        return self.item_code
    
    class Meta:
        abstract = True

class Item(AbstractItem):
    item_code = models.CharField(u"商品コード", max_length=256, unique=True)
    class Meta(AbstractItem.Meta):
        db_table = 'item'
        verbose_name = u"商品"
        verbose_name_plural = u"商品"

class OrderItem(AbstractItem):
    item_code = models.CharField(u"商品コード", max_length=256)
    buy_num = models.PositiveIntegerField(u"数量")
    order = models.ForeignKey('Order')

    class Meta(AbstractItem.Meta):
        db_table = 'order_item'
        verbose_name = u"商品"
        verbose_name_plural = u"商品"

class Order(models.Model):
    name = models.CharField(u"名前", max_length=256)
    address = models.CharField(u"住所", max_length=256)
    email = models.CharField(u"メールアドレス", max_length=256)
    order_time = models.DateTimeField(u"注文日時", auto_now_add=True)

    def __unicode__(self):
        return u"{} 様の注文".form(self.name)

    class Meta:
        db_table = 'order'
        verbose_name = u"注文"
        verbose_name_plural = u"注文"
