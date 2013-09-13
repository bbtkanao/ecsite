# coding: utf-8
class CartItem(object):
    def __init__(self, item_id=0, item_code=None, item_name=None, price=0, buy_num=0):
        self.item_id = item_id
        self.item_code = item_code
        self.item_name = item_name
        self.price = price
        self.buy_num = buy_num
