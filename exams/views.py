from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from .forms import ExamForm  # make sure you have this form created
from .forms import CourseForm, PaymentForm, ExamForm


def exam_dashboard(request):
    return render(request, 'exams/exam_dashboard.html')  # Make sure this template exists


def exams_dashboard(request):
    exams = Exam.objects.all()
    return render(request, 'exams/dashboard.html', {'exams': exams})

def add_exams(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exams_dashboard')  # redirect to exam list/dashboard
    else:
        form = ExamForm()
    
    return render(request, 'exams/add_exam.html', {'form': form})

def edit_exams(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exams_dashboard')
    else:
        form = ExamForm(instance=exam)
    
    return render(request, 'exams/edit_exam.html', {'form': form, 'exam': exam})

def delete_exams(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    if request.method == 'POST':
        exam.delete()
        return redirect('exams_dashboard')
    
    return render(request, 'exams/confirm_delete.html', {'exam': exam})
