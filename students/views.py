# students/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from students.models import Student, Course, Payment, Exam
from students.forms import StudentForm, CourseForm
from .models import AboutPage, ContactPage, Notice, Teacher
# -------------------------------
# Home & Dashboard Views
# -------------------------------

@login_required
def home(request):
    return render(request, 'students/home.html')

@login_required
def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'exam_count': Exam.objects.count(),
        'payment_count': Payment.objects.count(),
        'students': Student.objects.order_by('last_name'),
    }
    return render(request, 'students/dashboard.html', context)


# -------------------------------
# Student Views (CRUD + Dashboard)
# -------------------------------

@login_required
def students_dashboard(request):
    students = Student.objects.all()
    return render(request, 'students/students_dashboard.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('students:dashboard')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('students:dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('students:dashboard')
    return render(request, 'students/confirm_delete.html', {'student': student})


# -------------------------------
# Course Views (Public + Admin)
# -------------------------------

# Public views
def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'students/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'students/course_detail.html', {'course': course})

# Admin dashboard view
@login_required
def courses_dashboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Course.objects.filter(course_title__icontains=search_query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/dashboard.html', {'courses': courses})
def course_dashboard(request):
    # Your logic for listing courses
    return render(request, 'courses/courses_dashboard.html', context)
# CRUD views
@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('courses_dashboard')
    else:
        form = CourseForm()
    return render(request, 'students/add_course.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('courses_dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'students/edit_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect('courses_dashboard')
    return render(request, 'students/course_confirm_delete.html', {'course': course})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')  # or your actual list view name
    return render(request, 'students/course_confirm_delete.html', {'course': course})
# -------------------------------
# Exam & Payment Dashboards
# -------------------------------

@login_required
def exams_dashboard(request):
    exams = Exam.objects.select_related('course').all()
    return render(request, 'students/exams_dashboard.html', {'exams': exams})

@login_required
def payments_dashboard(request):
    payments = Payment.objects.select_related('student').all()
    return render(request, 'students/payments_dashboard.html', {'payments': payments})
def course_dashboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Course.objects.filter(course_title__icontains=search_query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/courses_board.html', {'courses': courses})
def courses_dashboard(request):
    # your code here
    return render(request, 'courses/dashboard.html')
def courses_dashboard(request):
    # your code here
    return render(request, 'courses/dashboard.html')
def course_dashboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Course.objects.filter(course_title__icontains=search_query)
    else:
        courses = Course.objects.all()
    return render(request, 'courses/courses_board.html', {'courses': courses})
@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'students/course_form.html', {'form': form})

@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # or another valid view name
    else:
        form = CourseForm(instance=course)
    return render(request, 'students/course_form.html', {'form': form})

def course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


# Create your views here.
def home(request):
    publicNotices = Notice.objects.filter(isPublic = True)
    data = {"public_notices": publicNotices}
    return render(request, 'home.html', data)

def about(request):
    about_text = AboutPage.objects.all()
    data = {"aboutDetails": about_text}
    return render(request, 'about.html', data)

def contact(request):
    contact_text = ContactPage.objects.all()
    data = {"contactDetails": contact_text}
    return render(request, 'contact.html', data)

def adminPanel(request):
    if 'admin_user' in request.session:
        all_students = Student.objects.all()
        all_teachers = Teacher.objects.all()
        data = {'students': all_students, 'teachers': all_teachers}
        return render(request, 'admin/admin_panel.html', data)
    else:
        return redirect('admin_login')


def adminLogin(request):
    if request.method == 'POST':
        admin_email = request.POST['email']
        admin_pwd = request.POST['pwd']

        if admin_email == "admin@gmail.com" and admin_pwd == "admin@123":
            request.session['admin_user'] = admin_email
            return redirect('admin_panel')
        else:
            return redirect('admin_login')

    return render(request, 'admin/admin_login.html')

def adminLogout(request):
    del request.session['admin_user']
    return redirect('admin_login')


def adminAbout(request):
    about_details = AboutPage.objects.all()
    data = {"aboutDetails": about_details}
    return render(request, 'admin/admin_about.html', data)

def updateAbout(request, id):
    if request.method == 'POST':
        aboutText = request.POST['text']
        about_obj = AboutPage.objects.get(id = id)
        about_obj.about = aboutText
        about_obj.save()
    return redirect('admin_about')

def adminContact(request):
    contact_details = ContactPage.objects.all()
    data = {"contactDetails": contact_details} 
    return render(request, 'admin/admin_contact.html', data)

def updateContact(request, id):
    if request.method == 'POST':
        contactAddress = request.POST['address']
        contactEmail = request.POST['email']
        contactNumber = request.POST['contact']
        contact_obj = ContactPage.objects.get(id = id)
        contact_obj.address = contactAddress
        contact_obj.email = contactEmail
        contact_obj.contact_num = contactNumber
        contact_obj.save()
    return redirect('admin_contact')


def addStudent(request):
    if request.method == 'POST':
        fullName = request.POST['full_name']
        fatherName = request.POST['f_name']
        motherName = request.POST['m_name']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        stuEmail = request.POST['stu_email']
        contactNum = request.POST['contact_number']
        dob = request.POST['dob']
        course = request.POST['course']
        studentId = request.POST['stu_id']
        studentUserName = request.POST['stu_user_name']
        studentPassword = request.POST['stu_pwd']

        add_student = Student.objects.create(full_name=fullName, father_name=fatherName, mother_name=motherName, gender=gender, address=address, city=city,email=stuEmail, contact_num=contactNum, date_of_birth=dob, course=course, stu_id=studentId, user_name=studentUserName, password=studentPassword)

        add_student.save()
    return render(request, 'admin/new_student.html')

def manageStudent(request):
    all_students = Student.objects.all()
    data = {"students": all_students}
    return render(request, 'admin/manage_students.html', data)


def updateStudent(request, id):
    if request.method == 'POST':
        student_obj = Student.objects.get(id=id)

        fullName = request.POST['full_name']
        fatherName = request.POST['f_name']
        motherName = request.POST['m_name']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        stuEmail = request.POST['stu_email']
        contactNum = request.POST['contact_number']
        dob = request.POST['dob'] or student_obj.date_of_birth
        course = request.POST['course'] or student_obj.course
        studentId = request.POST['stu_id']
        studentUserName = request.POST['stu_user_name']
        studentPassword = request.POST['stu_pwd']


        student_obj.full_name = fullName
        student_obj.father_name = fatherName
        student_obj.mother_name = motherName
        student_obj.gender = gender
        student_obj.address = address
        student_obj.city = city
        student_obj.email = stuEmail
        student_obj.contact_num = contactNum
        student_obj.date_of_birth = dob
        student_obj.course = course
        student_obj.stu_id = studentId
        student_obj.user_name = studentUserName
        student_obj.password = studentPassword

        student_obj.save()
    return redirect('manage_students')

def deleteStudent(request, id):
    if 'admin_user' in request.session:
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
    return redirect('manage_students')


def addNotice(request):
    if request.method == 'POST':
        noticeTitle = request.POST['notice_title']
        noticeContent = request.POST['notice_content']
        isPublic = request.POST['notice_status']

        add_notice = Notice.objects.create(title=noticeTitle, content=noticeContent, isPublic=isPublic)
        add_notice.save()
    return render(request, "admin/admin_notice.html")


def manageNotices(request):
    all_notices = Notice.objects.all()
    data = {'notices': all_notices}
    return render(request, 'admin/manage_notices.html', data)


def deleteNotice(request, id):
    if 'admin_user' in request.session:
        notice_obj = Notice.objects.get(id=id)
        notice_obj.delete()
    return redirect('manage_notices')

def updateNotice(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        status = request.POST['status']

        notice_obj = Notice.objects.get(id=id)
        notice_obj.title = title
        notice_obj.content = content
        notice_obj.isPublic = status

        notice_obj.save()
    return redirect('manage_notices')


def addTeacher(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        email = request.POST['email']
        contact_num = request.POST['contact_number']
        qualification = request.POST['qualification']

        add_teacher = Teacher.objects.create(full_name=full_name, gender=gender, email=email,contact_num=contact_num, qualification=qualification)
        add_teacher.save()
    return render(request, 'admin/add_teacher.html')

def manageTeachers(request):
    all_teachers = Teacher.objects.all()
    data = {"teachers": all_teachers}
    return render(request, 'admin/manage_teachers.html', data)

def deleteTeacher(request, id):
    teacher_obj = Teacher.objects.get(id=id)
    teacher_obj.delete()
    return redirect('manage_teachers')

def studentLogin(request):
    if 'student_user' not in request.session:
        if request.method == "POST":
            user_name = request.POST['userName']
            student_pwd = request.POST['stuPwd']

            stu_exists = Student.objects.filter(user_name=user_name, password=student_pwd).exists()
            if stu_exists:
                request.session['student_user'] = user_name
                return redirect('student_dashboard')

        return render(request, 'student/student_login.html')
    else:
        return redirect('student_dashboard')



def studentDashboard(request):
    if 'student_user' in request.session:
        student_in_session = Student.objects.get(user_name=request.session['student_user'])
        data  = {"student": student_in_session}
        return render(request, 'student/student_dashboard.html', data)
    else:
        return redirect('student_login')


def studentLogout(request):
    del request.session['student_user']
    return redirect('student_login')


def updateFaculty(request, id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        contactNumber = request.POST['contact_number']
        gender = request.POST['gender']
        qualification = request.POST['qualification']

        teacher_obj = Teacher.objects.get(id=id)
        teacher_obj.full_name = full_name
        teacher_obj.email = email
        teacher_obj.contact_num = contactNumber
        teacher_obj.gender = gender
        teacher_obj.qualification = qualification
        teacher_obj.save()
    return redirect('manage_teachers')


def viewNotices(request):
    if 'student_user' in request.session:
        student_notice = Notice.objects.filter(isPublic = False)
        data = {"notices": student_notice}
        return render(request, 'student/view_notices.html', data)
    else:
        return redirect('student_login')

def studentSettings(request):
    if 'student_user' in request.session:
        student_obj = Student.objects.get(user_name = request.session['student_user'])
        data = {'student': student_obj}
        if request.method == 'POST':
            currentPwd = request.POST['current_pwd']
            new_pwd = request.POST['new_pwd']
            student_obj.password  =new_pwd
            student_obj.save() 
            return redirect('student_dashboard')      
        return render(request, "student/student_settings.html", data)
    else:
        return redirect('student_login')