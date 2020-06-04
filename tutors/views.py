from .models import Tutor
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .serializers import TutorSerializer


class TutorDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutor_add.html'

    def get(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        serializer = TutorSerializer(tutor)
        return Response({'serializer': serializer, 'tutor': tutor})

    def post(self, request, pk):
        tutor = get_object_or_404(Tutor, pk=pk)
        serializer = TutorSerializer(tutor, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'tutor': tutor})
        serializer.save()
        return redirect('tutors')


class TutorList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutor_list.html'

    def get(self, request):
        queryset = Tutor.objects.all()
        return Response({'tutors': queryset})


class TutorCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutor_create.html'

    def get(self, request, *args, **kwargs):
        serializer = TutorSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = TutorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save(info=self.request.user)
        return redirect('tutors')
