from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.throttling import PreSingUpThrottle
from core.view import DTAPIView


class UserRegisterAPIView(DTAPIView):
    throttle_classes = (PreSingUpThrottle,)
    permission_classes = (AllowAny,)

    def post(self, request):
        return Response(status=status.HTTP_202_ACCEPTED)

    def put(self, request):
        return Response(status=status.HTTP_201_CREATED)