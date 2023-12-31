from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add_fortune', views.add_fortune, name='add_fortune')
]