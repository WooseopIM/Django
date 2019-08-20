from django.urls import path
from . import views

# 여러 목록별 중복 이름을 방지하기 위한 app_name 설정
app_name = 'posts'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/update/', views.update, name="update"),
]