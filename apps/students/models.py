
from django.db import models
from django.contrib.auth import get_user_model

from config import settings

User = get_user_model()




class Student(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    mother_name = models.CharField(max_length=100, blank=True, default="")
    registration_number = models.CharField(max_length=50, unique=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=100)
    address = models.TextField()

    image = models.ImageField(upload_to="student_images/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"