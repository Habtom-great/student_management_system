
from django import forms
from django.contrib.auth import get_user_model

from .models import Instructor, Course
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()
# --------------------------
# User Forms
# --------------------------
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# --------------------------
# Student Form
# --------------------------
class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# --------------------------
# Instructor Form
# --------------------------
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['user', 'bio']

# --------------------------
# Course Form
# --------------------------
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_code',
            'course_title',
            'course_subtitle',
            'description',
            'instructor',
            'department',
            'thumb_image',
            
        ]
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }


