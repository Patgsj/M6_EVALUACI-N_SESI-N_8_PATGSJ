from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inputbook/', views.input_book, name='inputbook'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
]
