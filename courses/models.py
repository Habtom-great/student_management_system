from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=20, default='DEFAULT001')
    course_title = models.CharField(max_length=200, default='Default Course Title')
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instructor = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='instructor_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_title
   
