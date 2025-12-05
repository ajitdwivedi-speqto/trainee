from django.db import models

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    rollno = models.IntegerField(unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username