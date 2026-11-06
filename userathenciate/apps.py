from django.apps import AppConfig


class UserathenciateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userathenciate'

    def ready(self):
        import userathenciate.signals
