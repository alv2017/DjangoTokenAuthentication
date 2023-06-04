from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutAllView as KnoxLogoutAllView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        tags=["auth"],
        operation_summary="Login and obtain authentication token",
        operation_description="Authenticates the user and returns the authentication token",
        request_body=AuthTokenSerializer,
        responses={status.HTTP_200_OK: AuthTokenSerializer},
    )
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class LogoutView(KnoxLogoutView):
    """Logs the user out of the current session, i.e. deletes the current session token for the user"""

    pass


class LogoutAllView(KnoxLogoutAllView):
    """Logs the user out of all opened sessions, i.e. deletes all auth tokens for the user"""

    pass
