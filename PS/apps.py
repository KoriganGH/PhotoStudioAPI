from django.apps import AppConfig


class PsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PS'
    verbose_name = 'PhotoStyle'

    def ready(self):
        import PS.signals
