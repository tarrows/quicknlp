from django.contrib import admin

from .models import Primitive, Rule
# Register your models here.


@admin.register(Primitive)
class PrimitiveAdmin(admin.ModelAdmin):
    pass


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass
