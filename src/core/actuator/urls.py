from django.urls import path

from core.actuator.views import ping_view

urlpatterns = [
    path('ping/', ping_view)
]