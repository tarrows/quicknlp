from rest_framework import routers
from .views import PrimitiveViewSet, RuleViewSet

router = routers.DefaultRouter()
router.register('primitives', PrimitiveViewSet)
router.register('rules', RuleViewSet)
