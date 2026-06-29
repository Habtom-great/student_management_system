from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def attendance_list(request):
    return render(request, "attendance/attendance_list.html")

def mark_attendance(request):
    return render(request, "attendance/mark_attendance.html")