"""GetTutored URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from parents.views import ParentList
from tutors.views import TutorList, TutorDetail, TutorCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parents/', ParentList.as_view(), name='parents'),
    path('', TutorList.as_view(), name='tutors'),
    path('tutor_add/<int:pk>/', TutorDetail.as_view(), name='tutor-add'),
    path('tutor_create/', TutorCreate.as_view(), name='tutor-create'),
]
