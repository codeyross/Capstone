from django.apps import AppConfig


class OnlybackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlybackend'

    def ready(self):
        import onlybackend.signals