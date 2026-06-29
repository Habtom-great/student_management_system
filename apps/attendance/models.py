from django.db import models
from django.conf import settings
from apps.courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)  # Present / Absent

    def __str__(self):
        return f"{self.student} - {self.course} - {self.status}"