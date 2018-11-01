from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)', views.detail),
    url(r'^link_page/$', views.link_page),
    url(r'^one_key_one_value/$', views.one_key_one_value),
    url(r'^one_key_more_value/$', views.one_key_more_value),
    url(r'^post_request_test/$', views.post_request_test),
    url(r'^post_request_test2/$', views.post_request_test2),
    url(r"^cook_test/$", views.cookie_test),
    url(r"^redirect1/$", views.redirect1),
    url(r"^redirect2/$", views.redirect2),
    url(r"^session1/$", views.session1),
    url(r"^session2/$", views.session2),
    url(r"^session2_handle/$", views.session2_handle),
    url(r"^session3/$", views.session3)


]
