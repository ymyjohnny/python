from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rec/(?P<recid>\d+)$', views.record, name='record'),
    url(r'^img/(?P<recid>\d+).jpg$', views.img_daytime, name='daytime'),
]

