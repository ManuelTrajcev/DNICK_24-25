# Generated by Django 5.1.3 on 2025-04-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flight2", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="airline",
            name="year_founder",
        ),
        migrations.AddField(
            model_name="airline",
            name="year_founded",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
