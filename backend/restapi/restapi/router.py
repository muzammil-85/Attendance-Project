from api.viewsets import *
from  rest_framework import routers

router = routers.DefaultRouter()
# router.register('employee',EmployeeViewset)
router.register('studentdetails',StudentDetailsViewset)
router.register('teacherdetails',TeacherDetailsViewset)
router.register('studentattendance',StudentAttendanceViewset)

# url will be like this :
#   localhost:8000/api/employee/
# methods are GET , POST , PUT , DELETE