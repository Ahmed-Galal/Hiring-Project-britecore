from django.conf.urls import url

from .views import risk,all_risk

urlpatterns = [
    url(r'^risk/(?P<company_id>[0-9]+)/(?P<risk_id>[0-9]+)/$', risk),
    url(r'^risk/(?P<company_id>[0-9]+)/$', all_risk)
]
