from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class ProblemType(TextChoices):
    Dump = "свалка", _("свалка")
    OversizeWaste = "крупногабаритные отходы", _("крупногабаритные отходы")
    OverflowingContainers = "переполненные контейнеры", _("переполненные контейнеры")
    OverflowingBins = "переполненные урны", _("переполненные урны")


class Status(TextChoices):
    StatusWait = "ожидание", _("ожидание")
    StatusOnCheck = "проверка", _("проверка")
    StatusRealization = "реализация", _("реализация")
    StatusDone = "выполнен", _("выполнен")
