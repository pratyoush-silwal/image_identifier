# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/<int:pk>/', views.upload_success, name='upload_success'),
]
