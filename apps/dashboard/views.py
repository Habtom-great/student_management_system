from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.courses.models import Enrollment
from apps.payments.models import Payment

# =========================
# ADMIN DASHBOARD
# =========================
@login_required
def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")


# =========================
# INSTRUCTOR DASHBOARD
# =========================
@login_required
def instructor_dashboard(request):
    return render(request, "dashboard/instructor_dashboard.html")


# =========================
# STUDENT DASHBOARD
# =========================

@login_required
def student_dashboard(request):

    student = request.user

    enrollments = Enrollment.objects.filter(student=student)
    payments = Payment.objects.filter(student__user=student)

    context = {
        "total_courses": enrollments.count(),
        "courses": [e.course for e in enrollments],
        "payments": payments,
    }

    return render(request, "students/student_dashboard.html", context)

# =========================
# HOME PAGE
# =========================
def home(request):
    return render(request, "dashboard/home.html")


