from django.urls import path
from . import views


urlpatterns = [
    path('classes', views.getClasses, name='classes'),
    path('items', views.getItems, name='items'),
]