from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles),
    path('new/', views.new),
    path('create/', views.create),
    path('index/', views.index),
]
