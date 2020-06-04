from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    GRADE_CHOICES = (
        ('primary', 'Primary'),
        ('juniors', 'Junior Secondary'),
        ('seniors', 'Senior Secondary'),
    )

    name = models.CharField(max_length=30)
    grade = models.CharField(choices=GRADE_CHOICES,
                             default='juniors', max_length=20)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    TITLE_CHOICES = (
        ('mr', 'Mr.'),
        ('ms', 'Miss.'),
        ('mrs', 'Mrs.'),
        ('master', 'Master.'),
        ('dr', 'Dr.'),
    )
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('fm', 'Female'),
    )
    MEDIUM_CHOICES = (
        ('online', 'Online Tutoring'),
        ('physical', 'Physical Tutoring'),
        ('both', 'Both'),
    )
    title = models.CharField(
        max_length=10, choices=TITLE_CHOICES, default='master')
    medium = models.CharField(
        max_length=10, choices=MEDIUM_CHOICES, default='online')
    info = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, default='m')
    expertise = models.ManyToManyField(Subject)
    description = models.TextField(max_length=1200, editable=True)
    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=11)
    address = models.CharField(max_length=200, verbose_name='Exact Address')
    state = models.CharField(max_length=20, verbose_name='State')
    local_govt = models.CharField(
        max_length=20, verbose_name='Local Government')
    isAvailable = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    price = models.IntegerField(
        verbose_name='Price per Month')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info.first_name
