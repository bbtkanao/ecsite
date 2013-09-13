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
from django.shortcuts import get_object_or_404, render
from itempage.models import Item

def item_page_display(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item.html', {'item': item})
