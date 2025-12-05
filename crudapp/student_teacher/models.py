from django.db import models
from django.conf import settings

# Create your models here.
class StudentDetails(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile',
        default=1,
        limit_choices_to={'is_staff': False}  # only normal users
    )
    rollno = models.IntegerField(unique=True,null=False)
    math_marks = models.IntegerField()
    science_marks = models.IntegerField()
    english_marks = models.IntegerField()
    history_marks = models.IntegerField()

    def __str__(self):
        return self.user.username