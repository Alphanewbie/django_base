from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.index, name="index"),
    path('insert/', views.insert, name="insert"),
    path('<int:pk>/', views.detail, name="detail"),
    path('posts/list/', views.get_all_post),
]
