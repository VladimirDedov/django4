from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<slug:cat_slug>/', views.categories, name='cats'),
]