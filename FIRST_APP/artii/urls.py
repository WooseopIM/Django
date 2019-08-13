from django.urls import path
from . import views
# .은 현재 폴더를 의미함.
# 새로 만들어준 지금 이 urls.py 파일은 artii 폴더에서 views.py와 같이 있음.

urlpatterns = [
    path('', views.artii),
    path('result/', views.artii_result)
]
