from rest_framework import viewsets
from . import models
from . import serializers

# class EmployeeViewset(viewsets.ModelViewSet):
#     queryset =  models.Employee.objects.all()
#     serializer_class = serializers.EmployeeSerializer

# this viewset automatically make some functions which are:
# create()
# retrieve() => only retrive one data
# list() => same as retrive but retrieve multiple data
# update()
# destroy()

class StudentDetailsViewset(viewsets.ModelViewSet):
    queryset =  models.Student_Details.objects.all()
    serializer_class = serializers.StudentDetailSerializer


class TeacherDetailsViewset(viewsets.ModelViewSet):
    queryset =  models.Teacher_Details.objects.all()
    serializer_class = serializers.TeacherDetailSerializer

class StudentAttendanceViewset(viewsets.ModelViewSet):
    queryset =  models.Student_Attendance.objects.all()
    serializer_class = serializers.StudentAttendanceSerializer
