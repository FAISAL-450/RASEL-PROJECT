from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    DEPARTMENT_CHOICES = [
        ('construction', 'Construction'),
        ('salesmarketing', 'Sales & Marketing'),
        ('finance', 'Finance'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_department_display()}"





