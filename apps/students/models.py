
from django.db import models
from django.conf import settings
from django.utils import timezone



class Student(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    

    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    sub_city = models.CharField(max_length=100, blank=True, null=True)
    woreda = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Payment(models.Model):

    STATUS = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    date = models.DateField()

    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return f"{self.student.full_name} - {self.amount}"