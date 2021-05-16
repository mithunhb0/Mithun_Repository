from django.urls import path
from moviesapp import views

urlpatterns = [
    path('homepage/',views.home_page),
    path('addmovie/',views.add_movie),
    path('movielist/',views.movie_list),
]
