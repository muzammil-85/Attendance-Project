# serializer are used manage the api , 
# which means that sending python queries in the form of json request to  external app or something


from rest_framework import serializers
from .models import *

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta: # all thing under this class become the object of above class.
#         model = Employee
#         fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Student_Details
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Teacher_Details
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Student_Attendance
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields

class SubjectTotalSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = SubjectTotal
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
