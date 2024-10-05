from django.urls import path
from memory_cards import views

urlpatterns = [
    path('', views.index, name='index'),
]