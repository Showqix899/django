from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_name=models.CharField(max_length=30)
    def __str__(self):
        return self.dept_name
class courses(models.Model):
    c_name=models.CharField(max_length=120)
    c_code=models.CharField(max_length=120)
    def __str__(self) -> str:
        return self.c_name


class students(models.Model):
    s_name=models.CharField(max_length=300)
    cgpa=models.DecimalField(max_digits=4,decimal_places=2)
    dept_name=models.ForeignKey(Dept,on_delete=models.CASCADE,null=True)
    c_name=models.ForeignKey(courses,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.s_name

class biodata(models.Model):
    s_name=models.ForeignKey(students,on_delete=models.CASCADE)
    address=models.CharField(max_length=300)
    email_contact=models.CharField(max_length=300)
    phon_contact=models.CharField(max_length=300)

    

   

