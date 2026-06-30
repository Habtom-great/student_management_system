from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
import openpyxl

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
            messages.success(request, "Student added successfully ✅")
            return redirect("students:student_list")
        else:
            messages.error(request, "Please correct the errors below ❌")

    return render(request, "students/add_student.html", {
        "form": form
    })

# EDIT
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully ✏️")
            return redirect("students:student_list")
        else:
            messages.error(request, "Update failed. Check inputs ❌")

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
        messages.success(request, "Student deleted successfully 🗑️")
        return redirect("students:student_list")

    return render(request, "students/delete_student.html", {
        "student": student
    })



def test(request):
    messages.success(request, "Hello message test")
    return redirect("students:student_list")


# EXPORT EXCEL
def export_excel(request):

    students = Student.objects.all()

    wb = Workbook()
    ws = wb.active
    ws.title = "Students"

    ws.append([
        "No",
        "Last Name",
        "Middle Name",
        "First Name",
        "Email",
        "Phone",
        "Department",
        "Semester",
        "Status"
    ])


    for i, student in enumerate(students, start=1):

        ws.append([
            i,
            student.last_name,
            student.middle_name,
            student.first_name,
            student.email,
            student.phone,
            getattr(student, "department", ""),
            getattr(student, "semester", ""),
            student.status
        ])


    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="students.xlsx"'


    wb.save(response)

    return response





# EXPORT PDF
def export_pdf(request):

    students = Student.objects.all()


    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = 'attachment; filename="students.pdf"'


    pdf = canvas.Canvas(response)


    pdf.setTitle("Students List")


    y = 800


    pdf.drawString(
        50,
        y,
        "Student Management System - Students List"
    )


    y -= 40


    for i, student in enumerate(students, start=1):

        text = (
            f"{i}. "
            f"{student.last_name} "
            f"{student.middle_name} "
            f"{student.first_name} "
            f"- {student.phone}"
        )


        pdf.drawString(
            50,
            y,
            text
        )

        y -= 20


        if y < 50:
            pdf.showPage()
            y = 800



    pdf.save()

    return response