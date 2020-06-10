from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.db.models import Q, Count

from .models import Tutor, Subject
from .serializers import TutorSerializer
from .permissions import IsOwnerOrReadOnly


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Tutro.objects.all()
    # Parameters to be sent to the backend
    name_contains_query = request.GET.get('name_contains')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    subject = request.GET.get('subject')
    grade = request.GET.get('grade')

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(
            Q(info__first_name__icontains=name_contains_query) |
            Q(info__last_name__icontains=name_contains_query)
        ).distinct()

    if is_valid_queryparam(price_min):
        qs = qs.filter(price__gte=price_min)

    if is_valid_queryparam(price_max):
        qs = qs.filter(price__lt=price_max)

    if is_valid_queryparam(expertise) and expertise != 'Choose...':
        qs = qs.filter(expertise__name=subject)

    if is_valid_queryparam(grade) and grade != 'Choose...':
        qs = qs.filter(expertise__grade=grade)

    return qs


class TutorList(generics.ListAPIView):
    """
    List all tutors.
    """
    serializer_class = TutorSerializer

    def get_queryset(self):
        qs = filter(self.request)
        return qs


class TutorCreate(generics.CreateAPIView):
    """
    Create a new tutor.
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


"""
def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return Journal.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Journal.objects.all().count():
        return False
    return True

class ReactInfiniteView(generics.ListAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        qs = infinite_filter(self.request)
        return qs

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "journals": serializer.data,
            "has_more": is_there_more_data(request)
        })
"""
