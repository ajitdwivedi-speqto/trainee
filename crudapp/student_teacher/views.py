from django.shortcuts import render, redirect
from student_teacher.models import StudentDetails
from student_teacher.form import StudentForm
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    detail=StudentDetails.objects.all()
    return render(request, 'home.html', {'students':detail})
def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=StudentForm()
    return render(request, 'form.html', {'form':form})
def edit_student(request, id):
    student=StudentDetails.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'form.html', {'form':StudentForm(instance=student)})
def delete_student(request, id):

    student=StudentDetails.objects.get(id=id)
    if student:
        student.delete()
        return redirect('home')
    else:
        return HttpResponse("Student not found")
    
    return render(request, 'home.html')

from rest_framework import viewsets
from student_teacher.serializers import StudentSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from student_teacher.permissions import IsAdminOrReadOnly
class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        if  self.request.user.is_staff:
            return StudentDetails.objects.all()
        return StudentDetails.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        operation_summary="Retrieve all students",
        security=[{'Bearer': []}],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    

    