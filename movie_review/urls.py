from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'movie_review'

urlpatterns = [
    path("", views.index, name='welcome_page'),
    path("instruction/", views.instructions, name='instructions'),
    path("movies/", views.movies_page, name='movies'),
    path("movie_button/", views.movie_play_button, name='movie_button'),
    path("analysis_page/", views.movie_analysis_button, name='movie_analysis_button'),
    path("analysis_page/", views.analysis, name='analysis_page'),


]
