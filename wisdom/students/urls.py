from django.urls import path
from .views import StudentsDash,FeedBackView,HandinView

urlpatterns = [
    path('studentsdash', StudentsDash.as_view(), name = 'studentsdash'),
    path('studentsfeedback', FeedBackView.as_view(), name= 'studentsfeedback'), 
    path('handin', HandinView.as_view(), name = 'handin'),
]
