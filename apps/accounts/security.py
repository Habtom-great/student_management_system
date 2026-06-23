from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


# ==========================================================
# ROLE CHECKERS
# ==========================================================
def is_admin(user):
    return user.is_authenticated and user.role == "admin"


def is_instructor(user):
    return user.is_authenticated and user.role == "instructor"


def is_student(user):
    return user.is_authenticated and user.role == "student"


# ==========================================================
# DECORATORS
# ==========================================================
def admin_required(view_func):
    return user_passes_test(is_admin, login_url="/accounts/login/")(view_func)


def instructor_required(view_func):
    return user_passes_test(is_instructor, login_url="/accounts/login/")(view_func)


def student_required(view_func):
    return user_passes_test(is_student, login_url="/accounts/login/")(view_func)


# ==========================================================
# SAFE REDIRECT (AUTO DASHBOARD ROUTING)
# ==========================================================
def role_redirect(user):
    if user.role == "admin":
        return "/dashboard/admin/"
    elif user.role == "instructor":
        return "/dashboard/instructor/"
    else:
        return "/dashboard/student/"