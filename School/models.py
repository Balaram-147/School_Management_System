from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name="schools", blank=True)
    teachers = models.ManyToManyField(Teacher, related_name="schools", blank=True)

    def __str__(self):
        return self.name

