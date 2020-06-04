from tutors.models import Tutor
from django.contrib.auth.models import User
from django.db import models


class Parent(models.Model):
    TITLE_CHOICES = (
        ('mr', 'Mr.'),
        ('ms', 'Miss.'),
        ('mrs', 'Mrs.'),
        ('master', 'Master.'),
        ('dr', 'Dr.'),
    )

    title = models.CharField(
        max_length=10, choices=TITLE_CHOICES, default='master')

    info = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, verbose_name='Exact Address')
    state = models.CharField(max_length=20, verbose_name='State')
    local_govt = models.CharField(
        max_length=20, verbose_name='Local Government')

    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=11)

    def __str__(self):
        return self.info.first_name


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return self.name


class TutorRequest(models.Model):
    MEDIUM_CHOICES = (
        ('online', 'Online Tutoring'),
        ('physical', 'Physical Tutoring'),
        ('both', 'Both'),
    )
    requested_tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, related_name='Requested_Tutor')

    medium = models.CharField(
        max_length=10, choices=MEDIUM_CHOICES, default='online')
    requested_by = models.ForeignKey(
        Parent, on_delete=models.CASCADE, related_name='Requested_By')

    requested_for = models.ForeignKey(
        Child, on_delete=models.CASCADE, related_name='Requested_For')

    requested_duration = models.PositiveIntegerField(
        verbose_name='Months_Needed')

    location_needed = models.CharField(
        max_length=200, verbose_name='Tutoring_Location')

    isAccepted = models.BooleanField(default=False)
    inProgress = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
