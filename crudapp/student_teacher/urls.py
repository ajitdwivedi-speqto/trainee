from django.urls import path, include
from student_teacher import views
from student_teacher.views import StudentViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'StudentDetails', StudentViewSet, basename='student')


urlpatterns = [
    path('', views.home_view, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('api/', include(router.urls)),  # API endpoints
]