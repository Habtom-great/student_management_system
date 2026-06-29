from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [

    # ================= PUBLIC =================
    path("", views.course_list, name="course_list"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # ================= DASHBOARD =================
    path("dashboard/", views.courses_dashboard, name="courses_dashboard"),

    # ================= COURSE DETAIL =================
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),

    # ================= ENROLLMENT =================
    path("course/<int:course_id>/enroll/", views.enroll_course, name="enroll_course"),
    path("course/<int:course_id>/unenroll/", views.unenroll_course, name="unenroll_course"),

    # ================= COURSE MANAGEMENT =================
    
    path("add/", views.add_course, name="add_course"),
    path("manage/", views.manage_courses, name="manage_courses"),

    path("course/<int:course_id>/edit/", views.edit_course, name="edit_course"),
    path("course/<int:course_id>/delete/", views.delete_course, name="delete_course"),

    # ================= INSTRUCTORS =================
    path("instructors/manage/", views.manage_instructors, name="manage_instructors"),
    path("instructors/add/", views.add_instructor, name="add_instructor"),
    path("instructors/<int:instructor_id>/edit/", views.edit_instructor, name="edit_instructor"),

    # ================= ACCOUNTING =================
    path("accounting/", views.accounting_details, name="accounting_details"),
]