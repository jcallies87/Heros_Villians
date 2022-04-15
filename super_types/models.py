from django.db import models

# Create your models here.

class Super(models.Model):
    type = models.CharField(max_length= 255) 