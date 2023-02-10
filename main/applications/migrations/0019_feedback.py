# Generated by Django 4.1.6 on 2023-02-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0018_remove_event_user_id_remove_news_author_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("message", models.TextField()),
                ("full_name", models.CharField(default="", max_length=500)),
                ("phone_number", models.CharField(default="", max_length=500)),
                ("created_date", models.DateField()),
            ],
            options={"abstract": False,},
        ),
    ]
