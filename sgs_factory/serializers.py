from rest_framework.serializers import ModelSerializer
from .models import City, Workshop, Team, Worker


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class WorkshopSerializer(ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
