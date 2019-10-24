from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update', views.update, name='update'),
    path('<int:movie_pk>/delete', views.delete, name='delete'),
    path('<int:movie_pk>/create_review', views.create_review, name='create_review'),
    path('<int:movie_pk>/like/', views.like, name="like"),
    path('<int:movie_pk>/dislike', views.dislike, name="dislike"),
    path('send_cookie/', views.send_cookie, name='send'),

]
