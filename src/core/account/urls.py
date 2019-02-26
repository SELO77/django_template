from django.urls import path

from core.account.views import UserRegisterAPIView


urlpatterns = [
    path('v1/register/', UserRegisterAPIView.as_view(), name='v1_register')
]
