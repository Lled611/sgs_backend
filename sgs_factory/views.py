from rest_framework.viewsets import ModelViewSet
from .models import City, Workshop, Team, Worker
from .serializers import CitySerializer, WorkshopSerializer, TeamSerializer, WorkerSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class WorkshopViewSet(ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
