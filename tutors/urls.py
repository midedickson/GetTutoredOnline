from django.urls import path
from tutors.views import *

urlpatterns = [
    path('tutor_list/', TutorList.as_view()),
    path('become_tutor/', TutorCreate.as_view()),
    path('tutors/<int:pk>/', TutorDetail.as_view()),
]
