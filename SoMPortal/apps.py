from django.apps import AppConfig


class SomportalConfig(AppConfig):
    name = 'SoMPortal'

    def ready(self):
        import SoMPortal.signals