from django.urls import path
from . import views

urlpatterns = [
    path('Home/',views.homepg),
    path('centers/', views.center_list, name='center_list'),
]
