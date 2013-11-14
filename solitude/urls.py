from django.conf.urls import include, patterns, url

from tastypie.api import Api

from lib.bango.urls import bango
from lib.delayable.resources import DelayableResource, ReplayResource
from lib.buyers.resources import (BuyerConfirmPinResource, BuyerPaypalResource,
                                  BuyerResetPinResource, BuyerResource,
                                  BuyerVerifyPinResource)
from lib.paypal.urls import paypal
from lib.sellers.resources import (SellerPaypalResource, SellerProductResource,
                                   SellerResource)
from lib.transactions.resources import TransactionResource

# Generic APIs
api = Api(api_name='generic')
api.register(BuyerResource())
api.register(BuyerConfirmPinResource())
api.register(BuyerVerifyPinResource())
api.register(BuyerResetPinResource())
api.register(SellerResource())
api.register(SellerProductResource())
api.register(TransactionResource())

# PayPal specific APIs
paypal.register(BuyerPaypalResource())
paypal.register(SellerPaypalResource())

# URLs to query delayed jobs.
delayable = Api(api_name='delay')
delayable.register(DelayableResource())
delayable.register(ReplayResource())

services_patterns = patterns('lib.services.resources',
    url(r'^settings/$', 'settings_list', name='services.settings'),
    url(r'^settings/(?P<setting>[^/<>]+)/$', 'settings_view',
        name='services.setting'),
    url(r'^error/', 'error', name='services.error'),
    url(r'^logs/', 'logs', name='services.log'),
    url(r'^status/', 'status', name='services.status'),
    url(r'^request/', 'request_resource', name='services.request'),
    url(r'^failures/transactions/', 'transactions_failures',
        name='services.failures.transactions'),
    url(r'^failures/statuses/', 'statuses_failures',
        name='services.failures.statuses'),
)


urlpatterns = patterns('',
    url(r'^proxy/', include('lib.proxy.urls')),
    url(r'^', include(api.urls)),
    url(r'^', include(paypal.urls)),
    url(r'^', include(bango.urls)),
    url(r'^bango/', include('lib.bango.urls')),
    url(r'^zippy/', include('lib.zippy.urls')),
    url(r'^', include(delayable.urls)),
    url(r'^$', 'solitude.views.home', name='home'),
    url(r'^provider/', include('lib.provider.urls')),
    url(r'^services/', include(services_patterns)),
)

handler500 = 'solitude.views.error'
handler404 = 'solitude.views.error_404'
handler403 = 'solitude.views.error_403'
