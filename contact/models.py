from django.db import models

# Create your models here.

class contact (models.Model):
    nam=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    onvan=models.CharField(max_length=50)
    matn=models.CharField(max_length=150)
