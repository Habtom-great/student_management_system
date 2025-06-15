from django.db import models
from django.contrib.auth.models import User
from courses.models import Course  # or wherever your Course model is


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Add this line
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.course} - {self.amount}"

