from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^item/(?P<item_id>\d+)/$', 'itempage.views.item_page_display'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^item_search$', 'itempage.views.item_search', name='item_search'),
                       url(r'^add_to_cart$', 'itempage.views.add_to_cart', name='add_to_cart'),
                       url(r'^cart$', 'itempage.views.cart_display', name='cart_display'),
    # Examples:
    # url(r'^$', 'ecsite.views.home', name='home'),
    # url(r'^ecsite/', include('ecsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
