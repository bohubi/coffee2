from django.conf.urls import url
from .views import *

app_name = "main"

urlpatterns = [
    # url(r'^$', index,name="index"),
    url(r'^home/$', home, name="home"),
    url(r'^createCoffee/$',createCoffee, name="createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name="editCoffee"),
]

