from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.contact, name="contact"),
    url(r'^sell$', views.contact_sell_create, name="contact_sell_create"),
    url(r'^buy$', views.contact_buy_create, name="contact_buy_create"),
]
