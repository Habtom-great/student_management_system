from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Instructor, Enrollment
from .forms import CourseForm, InstructorForm, StudentForm

#==========================
# PUBLIC COURSE VIEWS
#==========================
def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def public_courses(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'courses/course_list.html', {'courses': courses})
#==========================
# COURSE DASHBOARD (ROLE BASED)
#==========================
@login_required
def courses_dashboard(request):
    user = request.user

    if user.role == "admin":
        courses = Course.objects.all()

    elif user.role == "instructor":
        instructor = Instructor.objects.get(user=user)
        courses = Course.objects.filter(instructor=instructor)

    else:
        courses = Course.objects.filter(is_active=True)

    return render(request, 'courses/dashboard.html', {
        'courses': courses
    })
#==========================
# COURSE DETAIL + ENROLLMENT
#==========================
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    enrolled = False
    if request.user.role == "student":
        enrolled = Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists()

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'enrolled': enrolled
    })
#==========================
# INSTRUCTOR CREATE COURSE
#==========================
@login_required
def create_course(request):
    if request.user.role != "instructor":
        return redirect('courses_dashboard')

    instructor = Instructor.objects.get(user=request.user)

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = instructor
            course.save()

            messages.success(request, "Course created successfully!")
            return redirect('courses_dashboard')

    else:
        form = CourseForm()

    return render(request, 'courses/create_course.html', {'form': form})

#==========================
# STUDENT ENROLLMENT SYSTEM
#==========================
@login_required
def enroll_course(request, course_id):
    if request.user.role != "student":
        return redirect('courses_dashboard')

    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    messages.success(request, "Enrolled successfully!")
    return redirect('course_detail', course_id=course_id)

#==========================
#UNENROLL
#==========================
@login_required
def unenroll_course(request, course_id):
    if request.user.role != "student":
        return redirect('courses_dashboard')

    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.filter(
        student=request.user,
        course=course
    ).delete()

    messages.success(request, "Unenrolled successfully!")
    return redirect('course_detail', course_id=course_id)
#==========================
# ADMIN CRUD (COURSES)
#==========================
@login_required
def add_course(request):
    if request.user.role != "admin":
        return redirect('courses_dashboard')

    form = CourseForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Course added successfully!")
        return redirect('courses_dashboard')

    return render(request, 'courses/add_course.html', {'form': form})
#==========================
# INSTRUCTOR MANAGEMENT
#==========================
@login_required
def manage_instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors/manage_instructors.html', {
        'instructors': instructors
    })


def add_instructor(request):
    if request.user.role != "admin":
        return redirect('courses_dashboard')

    form = InstructorForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Instructor added successfully!")
        return redirect('manage_instructors')

    return render(request, 'instructors/add_instructor.html', {'form': form})

def edit_instructor(request, instructor_id):
    if request.user.role != "admin":
        return redirect('courses_dashboard')

    instructor = get_object_or_404(Instructor, id=instructor_id)
    form = InstructorForm(request.POST or None, instance=instructor)

    if form.is_valid():
        form.save()
        messages.success(request, "Instructor updated successfully!")
        return redirect('manage_instructors')

    return render(request, 'instructors/edit_instructor.html', {'form': form})

def course_list(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'courses/course_list.html', {'courses': courses})
def manage_courses(request):
    if request.user.role != "admin":
        return redirect('courses_dashboard')

    courses = Course.objects.all()
    return render(request, 'courses/manage_courses.html', {'courses': courses})
def course_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_view.html', {'course': course})

def edit_course(request, course_id):
    if request.user.role != "admin":
        return redirect('courses_dashboard')

    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)

    if form.is_valid():
        form.save()
        messages.success(request, "Course updated successfully!")
        return redirect('manage_courses')

    return render(request, 'courses/edit_course.html', {'form': form})

def delete_course(request, course_id):
    if request.user.role != "admin":
        return redirect('courses_dashboard')

    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect('manage_courses')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def accounting_details(request):
    chapters = [
        {"title": "Introduction", "subtitle": "What is accounting?"},
        {"title": "Double Entry", "subtitle": "Recording system"},
        {"title": "Financial Statements", "subtitle": "Reports & analysis"},
    ]

    return render(request, 'courses/accounting_details.html', {
        'chapters': chapters
    })



#==========================
# ACCOUNTING SPECIAL PAGE
#=========================
def accounting_details(request):
    chapters = [
        {"title": "Introduction", "subtitle": "What is accounting?"},
        {"title": "Double Entry", "subtitle": "Recording system"},
        {"title": "Financial Statements", "subtitle": "Reports & analysis"},
    ]

    return render(request, 'courses/accounting_details.html', {
        'chapters': chapters
    })

# ==========================
# Course Topic Specific Pages
# ==========================

def accounting_details(request):
    """Static content for accounting chapters."""
    chapters = [
        {"title": "Introduction", "subtitle": "What is accounting?"},
        {"title": "Basic Concepts", "subtitle": "Key accounting principles"},
        {"title": "Double Entry System", "subtitle": "Recording transactions"},
        {"title": "Trial Balance", "subtitle": "Checking accuracy"},
        {"title": "Adjusting Entries", "subtitle": "Adjustments before final reports"},
        {"title": "Financial Statements", "subtitle": "Income Statement, Balance Sheet"},
        {"title": "Cash Flow Statement", "subtitle": "Cash in and out"},
        {"title": "Bank Reconciliation", "subtitle": "Matching books with bank"},
        {"title": "Inventory Accounting", "subtitle": "Stock handling and valuation"},
        {"title": "Depreciation", "subtitle": "Asset usage and reduction"},
        {"title": "Budgeting", "subtitle": "Planning finances"},
        {"title": "Revision and Practice", "subtitle": "Final preparation"},
    ]
    return render(request, 'courses/accounting_details.html', {'chapters': chapters})
