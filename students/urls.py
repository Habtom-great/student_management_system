from django.urls import path
from . import views
from django.urls import include

app_name = 'courses'
urlpatterns = [
    # Home & Dashboard
    path('', views.home, name='home'),
    path('dashboard/', views.course_dashboard, name='dashboard'),
    path('students/dashboard/', views.students_dashboard, name='students_dashboard'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.course_dashboard, name='dashboard'),
    path('exams/dashboard/', views.exams_dashboard, name='exams_dashboard'),
    path('<int:pk>/view/', views.course_view, name='course_view'),
    path('list/<str:course_id>/', views.course_list, name='course_list'),
    # Students CRUD
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments_dashboard')),
    # Courses CRUD
    path('dashboard/', views.course_dashboard, name='dashboard'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_add'),
    path('courses/<int:pk>/edit/', views.course_update, name='course_edit'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),




    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('admin_panel/dashboard', views.adminPanel, name="admin_panel"),
    path('admin_panel/login/', views.adminLogin, name="admin_login"),

    path('admin_panel/logout/', views.adminLogout, name="admin_logout"),
    path('student/login/', views.studentLogin, name="student_login"),
    path('admin_panel/add_student/', views.addStudent, name="add_student"),
    path('admin_panel/about/', views.adminAbout, name="admin_about"),
    path('admin_panel/update_about/<str:id>/', views.updateAbout, name="update_about"),

    path('admin_panel/contact/', views.adminContact, name="admin_contact"),
    path('admin_panel/update_contact/<str:id>/', views.updateContact, name="update_contact"),
    path('admin_panel/manage_students/', views.manageStudent, name="manage_students"),
    path('admin_panel/update_student/<str:id>/', views.updateStudent, name="update_student"),
    path('admin_panel/delete_student/<str:id>/', views.deleteStudent, name="delete_student"),
    path('admin_panel/add_notice/', views.addNotice, name="add_notice"),

    path('admin_panel/manage_notices/', views.manageNotices, name="manage_notices"),
    path('admin_panel/delete_notice/<str:id>/', views.deleteNotice, name="delete_notice"),
    path('admin_panel/update_notice/<str:id>/', views.updateNotice, name="update_notice"),

    path('admin_panel/add_teacher/', views.addTeacher, name="add_teacher"),
    path('admin_panel/manage_teacher/', views.manageTeachers, name="manage_teachers"),
    path('admin_panel/delete_teacher/<str:id>/', views.deleteTeacher, name="delete_teacher"),

    path('student/dashboard/', views.studentDashboard, name="student_dashboard"),
    path('student/logout/', views.studentLogout, name="student_logout"),
    path('student/update_teacher/<str:id>/', views.updateFaculty, name="update_teacher"),
    path('student/view_notices/', views.viewNotices, name="view_notices"),
    path('student/student_settings/', views.studentSettings, name="student_settings")
   
]