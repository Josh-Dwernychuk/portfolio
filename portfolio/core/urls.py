from django.conf.urls import url
from portfolio.core import views


urlpatterns = [
    url(r'^', views.home, name='core'),
]
