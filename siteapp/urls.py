from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('alllist/', views.alllist),
    path('search/', views.search, name='search'),
]

# urlpatterns = [
#     path('main/', GetList.as_view(), name='main'),
# ]