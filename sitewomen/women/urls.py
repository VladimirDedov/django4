from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name = 'post')
]
