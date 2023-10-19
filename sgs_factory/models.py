from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, PROTECT
from django.db.models.constraints import UniqueConstraint
from django.core.validators import MinValueValidator


class City(Model):
    name = CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Workshop(Model):
    name = CharField(max_length=50)
    city = ForeignKey('City', related_name='city_workshops', on_delete=PROTECT)

    def __str__(self) -> str:
        return '%(city)s %(workshop)s' % {
            'city': self.city.name,
            'workshop': self.name
        }


class Team(Model):
    number = IntegerField(validators=[
        MinValueValidator(1)
    ])
    workshop = ForeignKey('Workshop', related_name='workshop_teams', on_delete=PROTECT)
    shift = BooleanField(default=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['number', 'workshop'], name='unique_workshop_team')
        ]

    def __str__(self) -> str:
        return str(self.number)


class Worker(Model):
    name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
