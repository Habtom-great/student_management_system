from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.courses.models import Course
from apps.instructors.models import Instructor
User = get_user_model()

# ==========================
# USER FORMS
# ==========================
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# ==========================
# STUDENT FORM
# ==========================
class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# ==========================
# INSTRUCTOR FORM
# ==========================
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['user', 'bio', 'phone']


# ==========================
# COURSE FORM
# ==========================


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']