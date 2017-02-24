from django.conf.urls import url
from . import views

urlpatterns = [
    #/index
    url(r'^$', views.index, name='index'),
    
    #packet/IP
    url(r'^(?P<ip_address>[0-9]+)/$', views.detail, name='detail'),
]
    