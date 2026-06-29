from django.shortcuts import render

from apps.attendance.models import Attendance

# Create your views here.
def student_dashboard(user):
    total_quizzes = Result.objects.filter(user=user).count()
    avg_score = Result.objects.filter(user=user).aggregate(Avg('score'))
    attendance_rate = Attendance.objects.filter(student=user).count()