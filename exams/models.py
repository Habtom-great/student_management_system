from django.db import models
from students.models import Student, Course, Payment, Exam  # ✅ correct

# Create your models here.


class Exam(models.Model):  # ← notice it's singular
    title = models.CharField(max_length=255)
    # other fields...
