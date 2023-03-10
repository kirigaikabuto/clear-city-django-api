# Generated by Django 4.1.6 on 2023-02-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0004_alter_application_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="address",
            field=models.CharField(blank=True, default="", max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="app_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ожидание", "ожидание"),
                    ("проверка", "проверка"),
                    ("реализация", "реализация"),
                    ("выполнен", "выполнен"),
                ],
                default="",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="app_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("свалка", "свалка"),
                    ("крупногабаритные отходы", "крупногабаритные отходы"),
                    ("переполненные контейнеры", "переполненные контейнеры"),
                    ("переполненные урны", "переполненные урны"),
                ],
                default="",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="created_date",
            field=models.CharField(blank=True, default="", max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="first_name",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="last_name",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="latitude",
            field=models.CharField(blank=True, default="", max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="longitude",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="message",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="patronymic",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="phone_number",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="photo_url",
            field=models.CharField(blank=True, default="", max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="user_id",
            field=models.CharField(blank=True, default="", max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="video_url",
            field=models.CharField(blank=True, default="", max_length=500, null=True),
        ),
    ]
