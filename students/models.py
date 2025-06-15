from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    duration_months = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Student(models.Model):
    REG_NO_PREFIX = "STD"
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    # Personal Information
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    # Demographic Information
    dob = models.DateField('Date of Birth', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    country = CountryField(blank=True, null=True)

    # Contact Information
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)

    # Academic Information
    registration_number = models.CharField(max_length=20, unique=True, editable=False)
    registration_date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='students')
    is_active = models.BooleanField(default=True)

    # Additional
    photo = models.ImageField(upload_to='students/photos/', blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def save(self, *args, **kwargs):
        if not self.registration_number:
            last_student = Student.objects.order_by('-id').first()
            last_id = last_student.id if last_student else 0
            self.registration_number = f"{self.REG_NO_PREFIX}{str(last_id + 1).zfill(5)}"
        super().save(*args, **kwargs)

    def full_name(self):
        names = [self.first_name]
        if self.middle_name:
            names.append(self.middle_name)
        names.append(self.last_name)
        return ' '.join(filter(None, names)).strip()

    def __str__(self):
        return f"{self.full_name()} ({self.registration_number})"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('CARD', 'Credit Card'),
        ('TRANSFER', 'Bank Transfer'),
        ('OTHER', 'Other'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='CASH')
    receipt_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-payment_date']
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"Payment #{self.receipt_number} - {self.student}"

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(max_length=100)
    exam_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    max_score = models.PositiveIntegerField(default=100)
    passing_score = models.PositiveIntegerField(default=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-exam_date']
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def __str__(self):
        return f"{self.course} - {self.name} ({self.exam_date.strftime('%Y-%m-%d')})"
    
class AboutPage(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about
from django.db import models

class AboutPage(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about

class ContactPage(models.Model):
    address = models.TextField()
    contact_num = models.CharField(max_length=20)  # use CharField for phone numbers
    email = models.EmailField()

    def __str__(self):
        return self.address

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=20)
    qualification = models.TextField()

    def __str__(self):
        return self.full_name
