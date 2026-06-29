from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    instructor = models.ForeignKey('instructors.Instructor', on_delete=models.SET_NULL, null=True)
    credits = models.IntegerField(default=3)
    description = models.TextField()
    category = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='courses/', null=True, blank=True)