from django.urls import path
from . import views

app_name = 'movie_review'

urlpatterns = [
    path("", views.index, name='frontpage'),
    path("thispage/", views.thispage, name='page'),
    path("apage/", views.apage),



]
