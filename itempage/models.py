# coding: utf-8
from django.db import models

class Item(models.Model):
    item_code = models.CharField(u"商品コード", max_length=256, unique=True)
    item_name = models.CharField(u"商品名", max_length=256)
    price = models.PositiveIntegerField(u"価格")

    def __unicode__(self):
        return self.item_code

    class Meta:
        db_table = 'item'
        verbose_name = u"商品"
        verbose_name_plural = u"商品"
