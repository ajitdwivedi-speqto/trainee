from django.contrib import admin
from student_teacher.models import StudentDetails
# Register your models here.
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'rollno', 'math_marks', 'science_marks', 'english_marks', 'history_marks')
    search_fields = ('rollno','user__username')
    list_filter = ('math_marks', 'science_marks', 'english_marks', 'history_marks')

admin.site.register(StudentDetails, StudentDetailsAdmin)
