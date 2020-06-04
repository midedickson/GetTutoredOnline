from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, permissions

from .models import Tutor
from .serializers import TutorSerializer
from .permissions import IsOwnerOrReadOnly


class TutorList(generics.ListAPIView):
    """
    List all tutors, or create a new tutor.
    """

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutorCreate(generics.CreateAPIView):
    """
    List all tutors, or create a new tutor.
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    def create(self, request, *args, **kwargs):
        # Copy parsed content from HTTP request
        data = request.data.copy()

        # Add id of currently logged user
        data['info'] = request.user.id

        # Default behavior but pass our modified data instead
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tutor.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
