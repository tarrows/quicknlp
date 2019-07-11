from django.db import models


class Primitive(models.Model):
    label = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __repr__(self):
        return f'{self.label}: {self.name}'

    __str__ = __repr__


class Rule(models.Model):
    label = models.CharField(max_length=128)
    syntactic = models.CharField(max_length=128)
    semantic = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.label} => {self.syntactic} {{{self.semantic}}}'

    __str__ = __repr__
