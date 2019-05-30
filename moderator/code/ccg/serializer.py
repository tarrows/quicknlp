from rest_framework import serializers
from .models import Primitive, Rule


class PrimitiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primitive
        fields = ('label', 'name')


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = ('label', 'syntactic', 'semantic', 'description')
