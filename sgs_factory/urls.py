from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, WorkshopViewSet, TeamViewSet, WorkerViewSet


router = DefaultRouter()
router.register(r'cities', CityViewSet, basename='city')
router.register(r'workshops', WorkshopViewSet, basename='workshop')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'workers', WorkerViewSet, basename='worker')
urlpatterns = [
    path('', include(router.urls))
]
