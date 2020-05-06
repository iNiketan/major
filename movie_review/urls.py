from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'movie_review'

urlpatterns = [
    url(r'^$', views.index, name='frontpage'),
    url(r'^thispage', views.thispage, name='page'),
    url(r'^apage', views.apage),



]
