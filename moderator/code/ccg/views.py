from rest_framework import viewsets
from .models import Primitive, Rule
from .serializer import PrimitiveSerializer, RuleSerializer


class PrimitiveViewSet(viewsets.ModelViewSet):
    queryset = Primitive.objects.all()
    serializer_class = PrimitiveSerializer


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
