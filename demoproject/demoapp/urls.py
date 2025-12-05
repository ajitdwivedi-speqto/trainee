from django.urls import path
from demoapp import views 

urlpatterns = [
    path('', views.demo_view, name='index'),
    path('upload/', views.upload_view, name='upload'),
]