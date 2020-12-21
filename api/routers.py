from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r"guess", viewsets.GuessViewSet)
router.register(r"trophy", viewsets.TrophyViewSet)
