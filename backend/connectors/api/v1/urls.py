from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135659ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135659", Testconnectors135659ViewSet, basename="testconnectors135659"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
