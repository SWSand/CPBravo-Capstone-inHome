# Generated by Django 5.0.4 on 2024-04-11 21:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property_app', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=10)),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('monthly_rent', models.DecimalField(decimal_places=2, max_digits=8)),
                ('lease_length', models.IntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='property_app.property')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rentals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('property', 'unit_number')},
            },
        ),
    ]
