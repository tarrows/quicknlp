from django.http import JsonResponse
from django.views import View
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import viewsets
from .models import Primitive, Rule
from .serializer import PrimitiveSerializer, RuleSerializer
from .services import derive


class PrimitiveViewSet(viewsets.ModelViewSet):
    queryset = Primitive.objects.all()
    serializer_class = PrimitiveSerializer


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


# class DerivationView(APIView):
#    def get(self, request):
#        q = request.GET.get('q', 'she has a book')
#        return Response(derive(q))
#
#    # HACK: https://stackoverflow.com/questions/49721089
#    # /django-viewset-has-not-attribute-get-extra-actions
#    @classmethod
#    def get_extra_actions(cls):
#        return []

class DerivationView(View):
    def get(self, request):
        q = request.GET.get('q', 'she has a book')
        return JsonResponse(derive(q))
