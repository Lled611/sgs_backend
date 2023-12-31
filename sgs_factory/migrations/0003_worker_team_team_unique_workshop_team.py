# Generated by Django 4.2.6 on 2023-10-19 10:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgs_factory', '0002_workshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('shift', models.BooleanField(default=True)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='workshop_teams', to='sgs_factory.workshop')),
            ],
        ),
        migrations.AddConstraint(
            model_name='team',
            constraint=models.UniqueConstraint(fields=('number', 'workshop'), name='unique_workshop_team'),
        ),
    ]
