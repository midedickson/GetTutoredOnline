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
    title = models.CharField(
        max_length=10, choices=TITLE_CHOICES, default='master')
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
    available = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    price = models.IntegerField(
        verbose_name='Price per Month')

    def __str__(self):
        return self.info.first_name
