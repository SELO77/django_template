from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'core.account'

    def ready(self):
        pass