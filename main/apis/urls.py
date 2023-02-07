from django.urls import include, re_path

app_name = "main"
urlpatterns = [
    re_path("v1/", include("main.applications.urls", namespace="applications"))
]
