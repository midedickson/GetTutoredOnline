from django.urls import path
from parents.views import *

urlpatterns = [
    path('become_parent/', ParentCreate.as_view()),
    path('parent/<int:pk>/', ParentDetail.as_view()),
]
