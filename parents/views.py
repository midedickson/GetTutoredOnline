from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from .models import Parent
from .serializers import ParentSerializer
from .permissions import IsOwner


class ParentCreate(generics.CreateAPIView):
    """
    Create a new parent.
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

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


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a parent.
    """
    permission_classes = [
        IsOwner,
    ]

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
