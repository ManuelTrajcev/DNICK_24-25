# Generated by Django 5.1.3 on 2025-04-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flight2", "0003_flightreport"),
    ]

    operations = [
        migrations.CreateModel(
            name="FlightLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flight_code", models.CharField(max_length=100)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("is_delete", models.BooleanField(default=False)),
                ("description", models.TextField()),
            ],
        ),
    ]
