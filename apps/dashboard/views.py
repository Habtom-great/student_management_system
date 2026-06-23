from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def admin_dashboard(request):
    return render(request, "dashboard/admin.html")


@login_required
def instructor_dashboard(request):
    return render(request, "dashboard/instructor.html")


@login_required
def student_dashboard(request):
    return render(request, "dashboard/student.html")
