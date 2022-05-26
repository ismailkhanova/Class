from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    # REQUIRED_FIELDS = ['is_student', 'is_teacher', 'email']  # By doing so create superuser command will ask their input

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
