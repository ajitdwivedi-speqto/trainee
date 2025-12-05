from django import forms
from student_teacher.models import StudentDetails

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['user', 'rollno', 'math_marks', 'science_marks', 'english_marks', 'history_marks']