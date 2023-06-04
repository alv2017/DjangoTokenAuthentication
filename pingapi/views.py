from django.conf import settings
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["ping"],
        operation_summary="API ping point, no authentication is required",
        operation_description="Shows API name, version, and access time",
    )
    def get(self, request):
        data = {
            "api": settings.API_NAME + " " + settings.API_VERSION,
            "ping": True,
            "current time": timezone.now().isoformat(timespec="seconds"),
        }
        return Response(data=data, status=status.HTTP_200_OK)


class RestrictedPingView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    @swagger_auto_schema(
        tags=["ping"],
        operation_summary="API ping point, authentication is required",
        operation_description="Shows API name, version, access time, and user welcome message",
    )
    def get(self, request):
        data = {
            "api": settings.API_NAME,
            "version": settings.API_VERSION,
            "message": f"Welcome, {request.user.username}!",
            "current time": timezone.now().isoformat(timespec="seconds"),
        }
        return Response(data=data, status=status.HTTP_200_OK)
