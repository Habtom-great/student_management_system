from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'code',
            'instructor',
            'credits',
            'description',
            'category',
            'thumbnail'
        ]