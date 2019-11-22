from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.funding_list, name="funding_list"),
    url(r'^send_funding_email$', views.send_funding_email, name="send_funding_email"),
]
