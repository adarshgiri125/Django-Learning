from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll = models.CharField(max_length = 14)
    address = models.TextField()
    age = models.IntegerField(max_length=2)
    file = models.FileField()

class Car(models.Model):
    name = models.CharField(max_length= 100)
    speed = models.IntegerField(default = 50)

    def __str__(self) -> str:
        return self.name



