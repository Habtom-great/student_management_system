from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from .security import admin_required, instructor_required, student_required

from apps.courses.models import Course, Enrollment
from apps.instructors.models import Instructor
from apps.students.models import Student


# ======================================================
# PUBLIC PAGES
# ======================================================

def home(request):
    return render(request, "accounts/home.html")


# ======================================================
# REGISTER
# ======================================================

def register_view(request):
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # validation
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("accounts:register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("accounts:register")

        # create user (IMPORTANT FIX)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password1
        )

        # split full name
        if full_name:
            parts = full_name.split(" ")
            user.first_name = parts[0]
            if len(parts) > 1:
                user.last_name = " ".join(parts[1:])
            user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html")


# ======================================================
# LOGIN
# ======================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        remember = request.POST.get("remember")

        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)

            messages.success(request, f"Welcome {user.first_name or user.username}")
            return redirect("accounts:dashboard")

        messages.error(request, "Invalid email or password.")

    return render(request, "accounts/login.html")


# ======================================================
# LOGOUT
# ======================================================

def logout_view(request):
    logout(request)
    return redirect("accounts:login")


# ======================================================
# ROLE REDIRECT
# ======================================================

@login_required
def role_redirect(request):

    role = getattr(request.user, "role", None)

    if role == "admin":
        return redirect("accounts:admin_dashboard")

    if role == "instructor":
        return redirect("accounts:instructor_dashboard")

    if role == "student":
        return redirect("accounts:student_dashboard")

    return redirect("accounts:home")


@login_required
def dashboard(request):
    return role_redirect(request)


# ======================================================
# ADMIN DASHBOARD
# ======================================================

@login_required
@admin_required
def admin_dashboard(request):

    context = {
        "total_students": Student.objects.count(),
        "total_courses": Course.objects.count(),
        "total_instructors": Instructor.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
    }

    return render(request, "dashboard/admin.html", context)


# ======================================================
# INSTRUCTOR DASHBOARD
# ======================================================

@login_required
@instructor_required
def instructor_dashboard(request):

    instructor = get_object_or_404(Instructor, user=request.user)
    courses = Course.objects.filter(instructor=instructor)

    return render(request, "dashboard/instructor.html", {
        "courses": courses,
        "total_courses": courses.count(),
        "total_students": Enrollment.objects.filter(course__instructor=instructor).count(),
    })


# ======================================================
# STUDENT DASHBOARD
# ======================================================

@login_required
@student_required
def student_dashboard(request):

    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, "dashboard/student.html", {
        "total_courses": enrollments.count(),
        "courses": [e.course for e in enrollments],
    })


# ======================================================
# ADMIN INSTRUCTOR MANAGEMENT
# ======================================================

@login_required
@admin_required
def admin_instructors(request):

    return render(request, "dashboard/admin_instructors.html", {
        "instructors": Instructor.objects.all()
    })


@login_required
@admin_required
def admin_instructor_detail(request, instructor_id):

    instructor = get_object_or_404(Instructor, pk=instructor_id)
    courses = Course.objects.filter(instructor=instructor)

    return render(request, "dashboard/admin_instructor_detail.html", {
        "instructor": instructor,
        "courses": courses,
    })


# ======================================================
# INSTRUCTOR COURSES
# ======================================================

@login_required
@instructor_required
def instructor_courses(request):

    instructor = get_object_or_404(Instructor, user=request.user)

    return render(request, "dashboard/instructor_courses.html", {
        "courses": Course.objects.filter(instructor=instructor)
    })


@login_required
@instructor_required
def instructor_course_detail(request, course_id):

    course = get_object_or_404(Course, pk=course_id)
    enrollments = Enrollment.objects.filter(course=course)

    return render(request, "dashboard/instructor_course_detail.html", {
        "course": course,
        "students": [e.student for e in enrollments],
    })


# ======================================================
# STUDENT COURSES
# ======================================================

@login_required
@student_required
def student_courses(request):

    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, "dashboard/student_courses.html", {
        "courses": [e.course for e in enrollments]
    })


@login_required
@student_required
def student_course_detail(request, course_id):

    enrollment = Enrollment.objects.filter(
        course_id=course_id,
        student=request.user
    ).first()

    if not enrollment:
        return render(request, "403.html", status=403)

    return render(request, "dashboard/student_course_detail.html", {
        "course": enrollment.course,
        "instructor": enrollment.course.instructor,
    })


# ======================================================
# REMOVE THIS (WRONG FUNCTION)
# ======================================================
# ❌ DELETE THIS - it was wrong:
# def PasswordResetDoneView(request):
#     enrollments = Enrollment.objects.filter(student=request.user)
#     return render(request, "dashboard/student_courses.html", {
#         "courses": [e.course for e in enrollments]
#     })