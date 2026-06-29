
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Student


def student_list(request):
    students = Student.objects.select_related("user").all()
    return render(request, "students/students_list.html", {"students": students})


def add_student(request):
    if request.method == "POST":

        # 1. Create User first
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            email=request.POST.get("email")
        )

        # 2. Create Student profile linked to user
        Student.objects.create(
            user=user,
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
        )

        return redirect("students:students_list")

    return render(request, "students/add_student.html")

def students_dashboard(request):
    return render(request, "students/student_dashboard.html")


def add_student(request):
    return render(request, "students/add_student.html")

def edit_student(request, student_id):
    return render(request, "students/edit_student.html", {"student_id": student_id})

def delete_student(request, student_id):
    return render(request, "students/delete_student.html", {"student_id": student_id})