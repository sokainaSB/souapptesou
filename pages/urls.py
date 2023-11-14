from django.urls import path
from . import views

urlpatterns = [
  path('', views.about, name='about'),
  path('2', views.pagetow, name='pagetow'),
]
