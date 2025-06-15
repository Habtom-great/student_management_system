# students/forms.py

from django import forms
from .models import Student  # Make sure Student model exists
from .models import Student, Course  # Make sure Course model is imported

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'duration_months', 'fee', 'description']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
