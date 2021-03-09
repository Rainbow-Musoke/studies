from django.contrib import admin
from .models import Course,StudentsDetail,TeacherAttendence,TeachersDetail,Units,Tuition

# Register your models here.
admin.site.register(Course)
admin.site.register(Tuition)
admin.site.register(StudentsDetail)
admin.site.register(TeacherAttendence)
admin.site.register(TeachersDetail)
admin.site.register(Units)