# coding: utf-8
from django.http import HttpResponse
from django.template import RequestContext, loader
from itempage.models import Item

def item_page_display(request, item_id):
    item = Item.objects.get(id=item_id)
    template = loader.get_template('item.html')
    context = RequestContext(request, {'item': item})
    html = template.render(context)
    return HttpResponse(html)
