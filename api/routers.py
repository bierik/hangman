from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r"guess_text", viewsets.GuessTextViewSet)
