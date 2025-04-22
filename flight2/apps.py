from django.apps import AppConfig


class Flight2Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "flight2"

    def ready(self):
        from . import singals

