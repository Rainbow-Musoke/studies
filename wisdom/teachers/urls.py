from django.urls import path
from .views import AttendenceView,AssingmentView,GradesView


urlpatterns = [
   path('grades', GradesView.as_view(), name = 'grades'),
   path('attendence', AttendenceView.as_view(), name = 'attendence'),
   path('assignments', AssingmentView.as_view(), name = 'assignment'),
]