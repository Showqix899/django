from django.db import models
from django.contrib.auth.models import User


class recipe(models.Model):
    options=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('snacks', 'Snacks'),
        ('dinner', 'Dinner'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    catagory=models.CharField(max_length=20,choices=options)
    images=models.ImageField(upload_to='images')
    description=models.TextField(max_length=100)
    ingrediant=models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    like=models.ManyToManyField(User,related_name="liked_recipes",blank=True)
    
    def __str__(self):
        return self.name
    def total_likes(self):
        return self.like.count()


