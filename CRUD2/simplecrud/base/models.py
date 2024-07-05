from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    def __str__(self):
        return self.dept_name
class student(models.Model):
    s_name = models.CharField(max_length=300)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.s_name