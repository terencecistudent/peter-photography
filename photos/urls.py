from django.urls import path
from photos import views

urlpatterns = [
    path('', views.index, name='index'),
]
