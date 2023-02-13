from django.db import models
from .common.entities import Status, ProblemType, ObjectType
from .common.models import Timestamped


class MainUser(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    first_name = models.CharField(
        max_length=255, default="", blank=True,
    )
    last_name = models.CharField(
        max_length=255, default="", blank=True,
    )
    username = models.CharField(
        max_length=255, default="", blank=True,
    )
    password = models.CharField(
        max_length=500, default="", blank=True,
    )
    email = models.CharField(
        max_length=500, default="", blank=True,
    )
    phone_number = models.CharField(
        max_length=500, default="", blank=True,
    )
    gender = models.CharField(
        max_length=500, default="", blank=True,
    )
    access_type = models.CharField(
        max_length=500, default="", blank=True,
    )
    avatar = models.CharField(
        max_length=500, default="", blank=True,
    )
    is_verified = models.BooleanField(
        default=False,
    )


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
    message = models.TextField(default="", blank=True,
                               )
    first_name = models.CharField(
        max_length=255, default="", blank=True,
    )
    last_name = models.CharField(
        max_length=255, default="", blank=True,
    )
    patronymic = models.CharField(
        max_length=255, default="", blank=True,
    )
    phone_number = models.CharField(
        max_length=255, default="", blank=True,
    )
    photo_url = models.CharField(
        max_length=500, default="", blank=True,
    )
    video_url = models.CharField(
        max_length=500, default="", blank=True,
    )
    address = models.CharField(
        max_length=600, default="", blank=True,
    )
    longitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    latitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    user = models.ForeignKey(
        to="MainUser", on_delete=models.CASCADE, default=""
    )
    created_date = models.DateField(
        max_length=400, default="", blank=True,
    )

    def __str__(self):
        return f"{self.id} | {self.app_type} | {self.app_status}"


class News(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    title = models.CharField(max_length=500, default="", blank=True)
    small_description = models.CharField(max_length=500, default="", blank=True)
    description = models.TextField(default="", blank=True)
    photo_url = models.CharField(max_length=600, default="", blank=True)
    author = models.ForeignKey(
        to="MainUser", on_delete=models.CASCADE, default=""
    )
    created_date = models.DateField(
    )


class Event(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    address = models.CharField(max_length=500, default="", blank=True)
    description = models.TextField(default="", blank=True)
    date = models.DateField(
        max_length=400, default="", blank=True
    )
    time = models.CharField(
        max_length=400, default="", blank=True
    )
    organizer_info = models.CharField(max_length=400, default="", blank=True)
    document_url = models.CharField(max_length=600, default="", blank=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    latitude = models.DecimalField(decimal_places=10, max_digits=100, default=0.0)
    user = models.ForeignKey(
        to="MainUser", on_delete=models.CASCADE, default=""
    )
    created_date = models.DateField(
        max_length=400, default="", blank=True
    )


class FileStorage(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    object_type = models.CharField(
        choices=ObjectType.choices,
        max_length=255, default="", blank=True
    )
    object_id = models.CharField(
        max_length=400, default="", blank=True
    )
    file_url = models.CharField(
        max_length=500, default="", blank=True
    )
    created_date = models.DateField(
        max_length=400, default="", blank=True
    )


class UserEvents(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    user = models.ForeignKey(
        to="MainUser", on_delete=models.CASCADE, default=""
    )
    obj_id = models.CharField(max_length=500, default="", blank=True)
    obj_type = models.CharField(
        choices=ObjectType.choices,
        max_length=255, default="", blank=True
    )
    created_date = models.DateField(

    )


class Comments(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    message = models.TextField()
    user = models.ForeignKey(
        to="MainUser", on_delete=models.CASCADE, default=""
    )
    obj_id = models.CharField(max_length=500, default="", blank=True)
    obj_type = models.CharField(
        choices=ObjectType.choices,
        max_length=255, default="", blank=True
    )
    created_date = models.DateField()


class Feedback(Timestamped):
    id = models.CharField(primary_key=True, max_length=500)
    message = models.TextField(blank=True)
    full_name = models.CharField(max_length=500, default="", blank=True)
    phone_number = models.CharField(max_length=500, default="", blank=True)
    created_date = models.DateField()
