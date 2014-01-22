from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from MACLibrary.views import *
from MACLibrary.models import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EzMAC.views.home', name='home'),
    # url(r'^EzMAC/', include('EzMAC.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', AddressListView.as_view()),
    url(r'^find/by-serial/(?P<pk>[-_\w]+)/$', AddressDetailView.as_view(), name='address-detail'),
    url(r'^find/by-mac/(?P<slug>[-_\w]+)/$', AddressDetailView.as_view(), name='address-detail'),
    url(r'^assign/by-serial/(?P<pk>[-_\w]+)/$', AssignAddressDetailView.as_view(), name='address-detail'),
    url(r'^assign/by-mac/(?P<slug>[-_\w]+)/$', AssignAddressDetailView.as_view(), name='address-detail'),
    url(r'^getnew/$', OpenAddressDetailView.as_view(), name='address-detail'),
    url(r'^freepending/$', free_pending_addresses_view, name='address-detail'),

)
