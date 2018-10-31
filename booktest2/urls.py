from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)', views.detail),
    url(r'^link_page/$', views.link_page),
    url(r'^one_key_one_value/$', views.one_key_one_value),
    url(r'^one_key_more_value/$', views.one_key_more_value)
]
