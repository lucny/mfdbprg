from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.FilmListView.as_view(), name='films_list'),
    path('films/genres/<str:genre_name>', views.FilmListView.as_view(), name='film_genre'),
    path('films/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('films/create', views.FilmCreate.as_view(), name='film_create'),
    path('films/<int:pk>/update', views.FilmUpdate.as_view(), name='film_update')
]