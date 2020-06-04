from rest_framework import serializers
from .models import *


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        exclude = ['info', 'isVerified', 'date_joined']

    def perform_create(self, serializer):
        serializer.save(info=self.request.user)
