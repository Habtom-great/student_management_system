from django import forms
from students.models import Course, Exam  # Import from students app
from payments.models import Payment        # Import from payments app
# students/forms.py
from django import forms

from students.models import Student  # ✅ Correct location of the Student model

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

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
