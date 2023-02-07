from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApplicationsConfig(AppConfig):
    name: str = "main.applications"
    verbose_name: str = _("applications")
