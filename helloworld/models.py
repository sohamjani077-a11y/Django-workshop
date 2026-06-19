from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

# Create your models here.
