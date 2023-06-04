from django.urls import path

from . import views

app_name = "pingapi"

urlpatterns = [
    path("", views.RestrictedPingView.as_view(), name="welcome"),
    path("ping/", views.PingView.as_view(), name="ping"),
]
