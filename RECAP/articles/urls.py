from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    path('<int:article_pk>/update', views.update, name="update"),
    path('<int:article_pk>/comments/', views.create_comment, name="comments"),
]