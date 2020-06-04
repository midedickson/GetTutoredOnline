from .models import Parent
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ParentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'parents.html'

    def get(self, request):
        queryset = Parent.objects.all()
        return Response({'parents': queryset})
