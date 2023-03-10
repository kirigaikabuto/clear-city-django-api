# Generated by Django 4.1.6 on 2023-02-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0002_application_created_at_application_modified_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="created_at",
                        verbose_name="created_at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="modified_at",
                        verbose_name="modified_at",
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=500, primary_key=True, serialize=False),
                ),
                ("address", models.CharField(max_length=500)),
                ("description", models.TextField()),
                ("date", models.CharField(max_length=400)),
                ("time", models.CharField(max_length=400)),
                ("organizer_info", models.CharField(max_length=400)),
                ("document_url", models.CharField(max_length=600)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=100)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=100)),
                ("user_id", models.CharField(max_length=400)),
                ("created_date", models.CharField(max_length=400)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="created_at",
                        verbose_name="created_at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="modified_at",
                        verbose_name="modified_at",
                    ),
                ),
                (
                    "id",
                    models.CharField(max_length=500, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=500)),
                ("small_description", models.CharField(max_length=500)),
                ("description", models.TextField()),
                ("photo_url", models.CharField(max_length=600)),
                ("author_id", models.CharField(max_length=600)),
                ("created_date", models.CharField(max_length=400)),
            ],
            options={"abstract": False,},
        ),
    ]
