from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=150)
    roll = models.IntegerField(unique=True)
    number = models.IntegerField()
    gpa = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.name}({self.roll})'
