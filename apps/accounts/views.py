from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .security import admin_required, instructor_required, student_required
from apps.courses.models import Course, Enrollment, Instructor


# ======================================================
# PUBLIC PAGES
# ======================================================

def home(request):
    return render(request, "accounts/home.html")


def register_view(request):
    return render(request, "accounts/register.html")


def profile_view(request):
    return render(request, "accounts/profile.html")


# ======================================================
# AUTHENTICATION
# ======================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect("accounts:role_redirect")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        remember = request.POST.get("remember")

        user = authenticate(
            request,
            username=email,      # change if your User model uses username
            password=password,
        )

        if user is not None:

            login(request, user)

            if not remember:
                request.session.set_expiry(0)

            return redirect("accounts:role_redirect")

        messages.error(request, "Invalid email or password.")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


# ======================================================
# ROLE REDIRECT
# ======================================================

@login_required
def role_redirect(request):

    if request.user.role == "admin":
        return redirect("admin_dashboard")

    elif request.user.role == "instructor":
        return redirect("instructor_dashboard")

    elif request.user.role == "student":
        return redirect("student_dashboard")

    return redirect("accounts:home")


# ======================================================
# PASSWORD PAGES
# ======================================================

def password_change_view(request):
    return render(request, "accounts/password_change.html")


def password_change_done_view(request):
    return render(request, "accounts/password_change_done.html")


def password_reset_view(request):
    return render(request, "accounts/password_reset.html")


def password_reset_done_view(request):
    return render(request, "accounts/password_reset_done.html")


def password_reset_confirm_view(request, uidb64, token):
    return render(request, "accounts/password_reset_confirm.html")


def password_reset_complete_view(request):
    return render(request, "accounts/password_reset_complete.html")


# ======================================================
# DASHBOARDS
# ======================================================

@login_required
@admin_required
def admin_dashboard(request):

    return render(request, "dashboard/admin.html")


@login_required
@instructor_required
def instructor_dashboard(request):

    return render(request, "dashboard/instructor.html")
@login_required
@student_required
def student_dashboard(request):

    enrollments = Enrollment.objects.filter(
        student=request.user
    )

    context = {
        "courses": enrollments.count(),
        "enrollments": enrollments
    }

    return render(
        request,
        "dashboard/student_dashboard.html",
        context
    )

@login_required
@student_required
def student_dashboard(request):

    return render(request, "dashboard/student_dashboard.html")


# ======================================================
# ADMIN
# ======================================================

@login_required
@admin_required
def admin_instructors(request):

    instructors = Instructor.objects.all()

    return render(
        request,
        "dashboard/admin_instructors.html",
        {"instructors": instructors},
    )


@login_required
@admin_required
def admin_instructor_detail(request, instructor_id):

    instructor = Instructor.objects.get(pk=instructor_id)

    courses = Course.objects.filter(instructor=instructor)

    return render(
        request,
        "dashboard/admin_instructor_detail.html",
        {
            "instructor": instructor,
            "courses": courses,
        },
    )


# ======================================================
# INSTRUCTOR
# ======================================================

@login_required
@instructor_required
def instructor_courses(request):

    courses = Course.objects.filter(instructor__user=request.user)

    return render(
        request,
        "dashboard/instructor_courses.html",
        {"courses": courses},
    )


@login_required
@instructor_required
def instructor_course_detail(request, course_id):

    course = Course.objects.get(pk=course_id)

    enrollments = Enrollment.objects.filter(course=course)

    students = [e.student for e in enrollments]

    return render(
        request,
        "dashboard/instructor_course_detail.html",
        {
            "course": course,
            "students": students,
        },
    )


# ======================================================
# STUDENT
# ======================================================

@login_required
@student_required
def student_courses(request):

    enrollments = Enrollment.objects.filter(student__user=request.user)

    return render(
        request,
        "dashboard/student_courses.html",
        {
            "courses": [e.course for e in enrollments]
        },
    )


@login_required
@student_required
def student_course_detail(request, course_id):

    enrollment = Enrollment.objects.filter(
        course_id=course_id,
        student__user=request.user,
    ).first()

    if enrollment is None:
        return render(request, "403.html", status=403)

    return render(
        request,
        "dashboard/student_course_detail.html",
        {
            "course": enrollment.course,
            "instructor": enrollment.course.instructor,
        },
    )

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.role == "admin":
            return redirect("admin_dashboard")
        elif request.user.role == "instructor":
            return redirect("instructor_dashboard")
        elif request.user.role == "student":
            return redirect("student_dashboard")
    return redirect("accounts:home")