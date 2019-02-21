from django.urls import path

from project.apps.actuator.views import ping_view

urlpatterns = [
    path('ping/', ping_view)
]