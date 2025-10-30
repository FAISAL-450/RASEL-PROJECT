from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    DEPARTMENT_CHOICES = [
        ('construction', 'Construction'),
        ('salesmarketing', 'Sales & Marketing'),
        ('finance', 'Finance'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        blank=True,
        null=True,
        help_text="Assigned department based on Azure AD email mapping"
    )

    def __str__(self):
        dept_display = self.get_department_display() if self.department else "Unassigned"
        return f"{self.user.username} - {dept_display}"

    def is_in_department(self, dept_key):
        return self.department == dept_key






