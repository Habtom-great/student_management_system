from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.courses.models import Course, Enrollment
from apps.instructors.models import Instructor

from .forms import CourseForm, InstructorForm


@login_required
def courses_dashboard(request):

    user = request.user

    if hasattr(user, "role") and user.role == "admin":
        courses = Course.objects.all()

    elif hasattr(user, "role") and user.role == "instructor":
        instructor = Instructor.objects.get(user=user)
        courses = Course.objects.filter(instructor=instructor)

    else:
        courses = Course.objects.all()

    return render(request, "courses/courses_dashboard.html", {
        "courses": courses
    })

# ======================================================
# STATIC PAGES
# ======================================================

def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


# ======================================================
# PUBLIC COURSE LIST (MAIN PAGE)
# ======================================================

def course_list(request):
    courses = Course.objects.all().order_by("-id")

    print("TOTAL COURSES:", courses.count())

    return render(request, "courses/course_list.html", {"courses": courses})
# ======================================================
# COURSE DETAIL
# ======================================================

@login_required
def course_detail(request, course_id):

    course = get_object_or_404(Course, id=course_id)

    enrolled = False
    if hasattr(request.user, "role") and request.user.role == "student":
        enrolled = Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists()

    return render(request, "courses/course_detail.html", {
        "course": course,
        "enrolled": enrolled
    })


# ======================================================
# ADD COURSE (INSTRUCTOR ONLY)
# ======================================================
@login_required
def add_course(request):

    form = CourseForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Course added successfully!")
        return redirect("courses:course_list")

    return render(request, "courses/add_course.html", {"form": form})


# ======================================================
# ENROLL / UNENROLL
# ======================================================

@login_required
def enroll_course(request, course_id):

    if request.user.role != "student":
        return redirect("courses:course_list")

    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    messages.success(request, "Enrolled successfully!")
    return redirect("courses:course_detail", course_id=course_id)


@login_required
def unenroll_course(request, course_id):

    if request.user.role != "student":
        return redirect("courses:course_list")

    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.filter(
        student=request.user,
        course=course
    ).delete()

    messages.success(request, "Unenrolled successfully!")
    return redirect("courses:course_detail", course_id=course_id)


# ======================================================
# ADMIN COURSE MANAGEMENT
# ======================================================

@login_required
def manage_courses(request):

    if request.user.role != "admin":
        return redirect("courses:course_list")

    courses = Course.objects.all().order_by("-id")

    return render(request, "courses/manage_courses.html", {
        "courses": courses
    })


@login_required
def edit_course(request, course_id):

    if request.user.role != "admin":
        return redirect("courses:course_list")

    course = get_object_or_404(Course, id=course_id)

    form = CourseForm(request.POST or None, request.FILES or None, instance=course)

    if form.is_valid():
        form.save()
        messages.success(request, "Course updated successfully!")
        return redirect("courses:manage_courses")

    return render(request, "courses/edit_course.html", {"form": form})


@login_required
def delete_course(request, course_id):

    if request.user.role != "admin":
        return redirect("courses:course_list")

    course = get_object_or_404(Course, id=course_id)
    course.delete()

    messages.success(request, "Course deleted successfully!")
    return redirect("courses:manage_courses")


# ======================================================
# INSTRUCTOR MANAGEMENT
# ======================================================

@login_required
def manage_instructors(request):

    if request.user.role != "admin":
        return redirect("courses:course_list")

    instructors = Instructor.objects.all()

    return render(request, "instructors/manage_instructors.html", {
        "instructors": instructors
    })


@login_required
def add_instructor(request):

    if request.user.role != "admin":
        return redirect("courses:course_list")

    form = InstructorForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Instructor added successfully!")
        return redirect("courses:manage_instructors")

    return render(request, "instructors/add_instructor.html", {"form": form})


@login_required
def edit_instructor(request, instructor_id):

    if request.user.role != "admin":
        return redirect("courses:course_list")

    instructor = get_object_or_404(Instructor, id=instructor_id)

    form = InstructorForm(request.POST or None, instance=instructor)

    if form.is_valid():
        form.save()
        messages.success(request, "Instructor updated successfully!")
        return redirect("courses:manage_instructors")

    return render(request, "instructors/edit_instructor.html", {"form": form})


# ======================================================
# ACCOUNTING STATIC PAGE
# ======================================================

def accounting_details(request):

    chapters = [
        {"title": "Introduction", "subtitle": "What is accounting?"},
        {"title": "Basic Concepts", "subtitle": "Key principles"},
        {"title": "Double Entry", "subtitle": "Recording transactions"},
        {"title": "Financial Statements", "subtitle": "Reports & analysis"},
        {"title": "Bank Reconciliation", "subtitle": "Matching records"},
        {"title": "Depreciation", "subtitle": "Asset reduction"},
        {"title": "Final Review", "subtitle": "Practice & revision"},
    ]

    return render(request, "courses/accounting_details.html", {
        "chapters": chapters
    })
