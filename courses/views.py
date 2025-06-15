from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course
from django.conf import settings

# --- General/Dashboard Views ---

@login_required
def dashboard(request):
    return redirect('courses:courses_dashboard')

@login_required
def courses_dashboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Course.objects.filter(course_title__icontains=search_query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/dashboard.html', {'courses': courses})

@login_required
def exams_dashboard(request):
    return render(request, 'exams/exams_dashboard.html')

@login_required
def payments_dashboard(request):
    return render(request, 'payments/dashboard.html')


# --- Course CRUD ---

@login_required
def add_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course_title = request.POST.get('course_title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        instructor = request.POST.get('instructor')
        department = request.POST.get('department')
        photo = request.FILES.get('photo')

        Course.objects.create(
            course_id=course_id,
            course_title=course_title,
            subtitle=subtitle,
            description=description,
            instructor=instructor,
            department=department,
            photo=photo,
        )
        messages.success(request, "Course added successfully!")
        return redirect('courses:courses_dashboard')

    return render(request, 'courses/add_course.html')


@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    return render(request, 'courses/edit_course.html', {'course': course})


@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect('courses:course_list')

def principles_accounting_view(request):
    return render(request, 'courses/accounting_details.html')
# --- Public Course Views ---

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


def course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course': course})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})
def view_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if course.course_title.lower() == "principles ofhhhh accounting":
        return render(request, 'courses/accounting_details.html', {'course': course})
    return render(request, 'courses/view_course.html', {'course': course})


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_edit.html', {'course': course})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect('courses:all_courses')


# --- Course Topic Specific Pages ---

def web_detail(request):
    course = get_object_or_404(Course, course_title="Web Development")
    return render(request, 'courses/web_dev_detail.html', {'course': course})


def accounting_detail(request):
    course = get_object_or_404(Course, course_title="PrincipllllAccounting")
    return render(request, 'courses/accounting_detail.html', {'course': course})


def accounting_details(request):
    # Static content for the accounting chapters
    chapter_titles = {
        1: 'Introduction',
        2: 'Basic Concepts',
        3: 'Double Entry System',
        4: 'Trial Balance',
        5: 'Adjusting Entries',
        6: 'Financial Statements',
        7: 'Cash Flow Statement',
        8: 'Bank Reconciliation',
        9: 'Inventory Accounting',
        10: 'Depreciation',
        11: 'Budgeting',
        12: 'Revision and Practice',
    }

    chapter_subtitles = {
        1: 'What is accounting?',
        2: 'Key accounting principles',
        3: 'Recording transactions',
        4: 'Checking accuracy',
        5: 'Adjustments before final reports',
        6: 'Income Statement, Balance Sheet',
        7: 'Cash in and out',
        8: 'Matching books with bank',
        9: 'Stock handling and valuation',
        10: 'Asset usage and reduction',
        11: 'Planning finances',
        12: 'Final preparation',
    }

    context = {
        'chapter_range': range(1, 13),
        'chapter_titles': chapter_titles,
        'chapter_subtitles': chapter_subtitles,
    }

    return render(request, 'courses/accounting-details.html', context)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})