from django.db import models

# Create your models here.
# class Employee(models.Model):
#     # TABLE ROWS
#     fullname = models.CharField(max_length=100)
#     emp_code = models.CharField(max_length=3)
#     mobile = models.CharField(max_length=15)

    # CREATE / INSERT / ADD - POST
    # RETRIEVE / FETCH - GET
    # UPDATE / EDIT - PUT
    # DELETE / REMOVE - DELETE

class Student_Details(models.Model):
    admission_no = models.CharField(max_length=100,blank=True,primary_key=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    year = models.IntegerField(null=True,blank=True)
    roll_no = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)


class Teacher_Details(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    unique_code = models.CharField(max_length=100,null=True,blank=True)

class Student_Attendance(models.Model):
    admission_no = models.ForeignKey(Student_Details,on_delete=models.CASCADE)
    subject = models.ForeignKey(Teacher_Details,on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

class SubjectTotal(models.Model):
    subject = models.ForeignKey(Teacher_Details,on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)