# coding: utf-8
from django import forms

class ItemSearchForm(forms.Form):
    item_name = forms.CharField()

class CartForm(forms.Form):
    item_id = forms.IntegerField()
    buy_num = forms.IntegerField()

class OrderForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()
