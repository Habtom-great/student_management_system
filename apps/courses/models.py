from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    thumb_image = models.ImageField(upload_to="courses/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    instructor = models.ForeignKey(
        "instructors.Instructor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} → {self.course}"