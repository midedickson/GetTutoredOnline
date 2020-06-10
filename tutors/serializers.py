from rest_framework import serializers
from .models import *


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class TutorSerializer(serializers.ModelSerializer):
    info = StringSerializer(many=False)
    expertise = StringSerializer(many=True)

    class Meta:
        model = Tutor
        fields = '__all__'
