from django.conf.urls import include, patterns, url

from rest_framework.routers import SimpleRouter

from .resources import TransactionViewSet

drf = SimpleRouter()
drf.register('transactions', TransactionViewSet, base_name='transactions')

urlpatterns = patterns('',
    url(r'^', include(drf.urls)),
)
