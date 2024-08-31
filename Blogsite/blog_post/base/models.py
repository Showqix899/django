from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    SUBJECT_CHOICES = [
        ('POLITICAL', 'Political'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('ECONOMICS', 'Economics'),
        ('EDUCATION', 'Education'),
        ('SCIENCE', 'Science'),
        ('SPORTS', 'Sports'),
        ('INTERNATIONAL', 'International'),
        ('COOKING', 'Cooking'),
        ('WEATHER', 'Weather'),
        ('TECH', 'Tech'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='images',null=True,blank=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=100)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


