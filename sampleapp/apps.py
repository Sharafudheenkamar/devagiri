from django.apps import AppConfig


class SampleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sampleapp'
def ready(self):
    import sampleapp.signals
