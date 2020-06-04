from rest_framework import serializers
from .models import *


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        exclude = ['info']

    def perform_create(self, serializer):
        serializer.save(info=self.request.user)
