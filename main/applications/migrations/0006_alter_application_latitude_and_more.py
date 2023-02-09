# Generated by Django 4.1.6 on 2023-02-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0005_alter_application_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="latitude",
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name="application",
            name="longitude",
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name="event",
            name="latitude",
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name="event",
            name="longitude",
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=100),
        ),
    ]