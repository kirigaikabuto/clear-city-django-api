from django.db import models
from .common.entities import Status, ProblemType
from .common.models import Timestamped


class Application(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    app_type = models.CharField(
        choices=ProblemType.choices,
        max_length=255
    )
    app_status = models.CharField(
        choices=Status.choices,
        max_length=255,
    )
    message = models.TextField(
    )
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    patronymic = models.CharField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=255
    )
    photo_url = models.CharField(
        max_length=500
    )
    video_url = models.CharField(
        max_length=500
    )
    address = models.CharField(
        max_length=600
    )
    longitude = models.CharField(
        max_length=255
    )
    latitude = models.CharField(
        max_length=300
    )
    user_id = models.CharField(
        max_length=400
    )
    created_date = models.CharField(
        max_length=400
    )


class News(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    title = models.CharField(max_length=500)
    small_description = models.CharField(max_length=500)
    description = models.TextField()
    photo_url = models.CharField(max_length=600)
    author_id = models.CharField(max_length=600)
    created_date = models.CharField(
        max_length=400
    )


class Event(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    address = models.CharField(max_length=500)
    description = models.TextField()
    date = models.CharField(
        max_length=400
    )
    time = models.CharField(
        max_length=400
    )
    organizer_info = models.CharField(max_length=400)
    document_url = models.CharField(max_length=600)
    longitude = models.DecimalField(decimal_places=6, max_digits=100)
    latitude = models.DecimalField(decimal_places=6, max_digits=100)
    user_id = models.CharField(
        max_length=400
    )
    created_date = models.CharField(
        max_length=400
    )
