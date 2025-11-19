from django.db import models

class Question(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    text = models.TextField()
    correct_answer = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200, default="")
    option_b = models.CharField(max_length=200, default="")
    option_c = models.CharField(max_length=200, default="")
    option_d = models.CharField(max_length=200, default="")
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='medium')
    subject = models.CharField(max_length=100, default='General')