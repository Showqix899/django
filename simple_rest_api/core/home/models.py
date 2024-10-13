from django.db import models

# Create your models here.

#person's color table
class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


#persons table
class Person(models.Model):
    name=models.CharField(max_length=100)

    age=models.IntegerField()

    color=models.ForeignKey(Color,null=True, blank=True,on_delete=models.CASCADE,related_name="color") #adding a foreign key ( Person -> Color)

    def __str__(self):
        return self.name
    
