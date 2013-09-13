# coding: utf-8
"""
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from itempage.models import Item

def item_page_display(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404

    template = loader.get_template('item.html')
    context = RequestContext(request, {'item': item})
    html = template.render(context)
    return HttpResponse(html)
"""
from django.shortcuts import get_object_or_404, render, redirect
from itempage.models import Item
from itempage.forms import ItemSearchForm, CartForm
from itempage.cart import CartItem

def item_page_display(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = CartForm(initial={'item_id': item.id, 'buy_num': 1})
    return render(request, 'item.html', {'item': item, 'form': form})

def item_search(request):
    form = ItemSearchForm(request.GET)
    if form.is_valid():
        items = Item.objects.filter(item_name=form.cleaned_data['item_name'])
    else:
        items = None

    return render(request, 'item_search.html', {'form': form, 'items': items})

def add_to_cart(request):
    form = CartForm(request.POST)
    if form.is_valid():
        item = Item.objects.get(id=form.cleaned_data['item_id'])
        cart_item_list = request.session.get('cart_item_list', [])
        cart_item = CartItem(item_id=item.id,
                             item_code=item.item_code,
                             item_name=item.item_name,
                             price=item.price,
                             buy_num=form.cleaned_data['buy_num']
                             )
        cart_item_list.append(cart_item)
        request.session['cart_item_list'] = cart_item_list
    return redirect('cart_display')

def cart_display(request):
    cart_item_list = request.session.get('cart_item_list', [])
    return render(request, 'cart.html', {'cart_item_list': cart_item_list})
