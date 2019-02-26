from django.apps import AppConfig


class ActuatorConfig(AppConfig):
    name = 'core.actuator'

    def ready(self):
        pass
