from django.db import models
from .common.entities import Status, ProblemType
from .common.models import Timestamped


class Application(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    app_type = models.CharField(
        choices=ProblemType.choices,
        max_length=255, default="",
    )
    app_status = models.CharField(
        choices=Status.choices,
        max_length=255,
        default="", null=True, blank=True,
    )
    message = models.TextField(default="",
                               )
    first_name = models.CharField(
        max_length=255, default="",
    )
    last_name = models.CharField(
        max_length=255, default="",
    )
    patronymic = models.CharField(
        max_length=255, default="",
    )
    phone_number = models.CharField(
        max_length=255, default="",
    )
    photo_url = models.CharField(
        max_length=500, default="",
    )
    video_url = models.CharField(
        max_length=500, default="",
    )
    address = models.CharField(
        max_length=600, default="",
    )
    longitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    latitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    user_id = models.CharField(
        max_length=400, default="",
    )
    created_date = models.CharField(
        max_length=400, default="",
    )


class News(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    title = models.CharField(max_length=500, default="")
    small_description = models.CharField(max_length=500, default="")
    description = models.TextField(default="")
    photo_url = models.CharField(max_length=600, default="")
    author_id = models.CharField(max_length=600, default="")
    created_date = models.CharField(
        max_length=400, default=""
    )


class Event(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    address = models.CharField(max_length=500, default="")
    description = models.TextField(default="")
    date = models.DateField(
        max_length=400, default=""
    )
    time = models.CharField(
        max_length=400, default=""
    )
    organizer_info = models.CharField(max_length=400, default="")
    document_url = models.CharField(max_length=600, default="")
    longitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    latitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    user_id = models.CharField(
        max_length=400, default=""
    )
    created_date = models.DateField(
        max_length=400, default=""
    )
