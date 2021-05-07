from django.db import models

# Create your models here.

class Coursedetails(models.Model):
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=200)
    coursename = models.CharField(max_length=200)
    sectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=200)
    instructorname = models.CharField(max_length=200)

class Studentdetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    gpa = models.IntegerField()

class Enrollment(models.Model):
    studentname = models.CharField(max_length=200)
    coursename = models.CharField(max_length=200)
