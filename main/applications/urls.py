from typing import Tuple

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ListApplicationsApi, CreateApplicationApi, UpdateApplicationApi
)

app_name = "applications"
router = DefaultRouter()
urlpatterns: Tuple = router.urls

applications_patterns: Tuple[str, ...] = (
    path("applications/list/", ListApplicationsApi.as_view(), name="application-list"),
    path("applications/create/", CreateApplicationApi.as_view(), name="application-create"),
    path("applications/update/", UpdateApplicationApi.as_view(), name="application-update"),

)

urlpatterns += (
    applications_patterns
)
