from django.shortcuts import render

# Create your views here.

from students.models import Student
from courses.models import Course
from exams.models import Exam
from payments.models import Payment

def home(request):
    context = {
        "students_count": Student.objects.count(),
        "courses_count": Course.objects.count(),
        "exams_count": Exam.objects.count(),
        "payments_count": Payment.objects.count(),
    }
    return render(request, "dashboard/home.html", context)
