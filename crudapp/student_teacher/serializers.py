from rest_framework import serializers
from student_teacher.models import StudentDetails
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    class Meta:
        model = StudentDetails
        fields = '__all__'
