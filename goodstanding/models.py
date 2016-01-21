from django.db import models

# Create your models here.

class gsUser(models.Model):
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    current = models.BooleanField()

class gsClass(models.Model):
    classCode = models.CharField(max_length=10)
    className = models.CharField(max_length=50)
    year = models.IntegerField()
    teacher = models.ForeignKey(gsUser)
    cohort = models.IntegerField()
    current = models.BooleanField()

class gsStudent(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    cohort = models.IntegerField()
    current = models.BooleanField()

class gsClassStudent(models.Model):
    gsClass = models.ForeignKey(gsClass)
    gsStudent = models.ForeignKey(gsStudent)


class gsClassStudentNote(models.Model):
    classStudent = models.ForeignKey(gsClassStudent)
    value = models.IntegerField()
    note = models.TextField()

