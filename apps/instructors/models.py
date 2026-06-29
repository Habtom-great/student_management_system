from django.db import models
from django.conf import settings


from django.db import models
from django.conf import settings


class Instructor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="instructor_profile",
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=100, blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    bio = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="instructors/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



