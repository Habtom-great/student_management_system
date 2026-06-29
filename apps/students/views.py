from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm


# DASHBOARD
def student_dashboard(request):
    return render(request, "students/student_dashboard.html")


# LIST
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {
        "students": students
    })


# ADD
@login_required
def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("student_list")

    return render(request, "students/student_form.html", {
        "form": form
    })


# EDIT
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("student_list")

    return render(request, "students/edit_student.html", {
        "form": form,
        "student": student
    })


# DETAIL
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    exams = [
        {"name": "Math", "score": 85},
        {"name": "Physics", "score": 78},
        {"name": "English", "score": 92},
    ]

    return render(request, "students/student_detail.html", {
        "student": student,
        "exams": exams
    })


# DELETE (simple version)
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/delete_student.html", {
        "student": student
    })