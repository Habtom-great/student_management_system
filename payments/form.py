from django import forms
from .models import Course, Payment, Exam

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'exam_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

