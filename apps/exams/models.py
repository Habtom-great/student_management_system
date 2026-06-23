from django.db import models


class Exam(models.Model):

    EXAM_TYPE_CHOICES = [
        ('quiz', 'Quiz'),
        ('midterm', 'Midterm Exam'),
        ('final', 'Final Exam'),
    ]

    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE_CHOICES, default='midterm')
    date = models.DateField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.title