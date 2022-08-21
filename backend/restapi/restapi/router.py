from api.viewsets import *
from  rest_framework import routers

router = routers.DefaultRouter()
# router.register('employee',EmployeeViewset)
router.register('student_details',StudentDetailsViewset)
router.register('teacher_details',TeacherDetailsViewset)
router.register('student_attendance',StudentAttendanceViewset)
router.register('subject_total',SubjectTotalViewset)

# url will be like this :
#   localhost:8000/api/employee/
# methods are GET , POST , PUT , DELETE