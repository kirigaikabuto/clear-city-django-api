# Generated by Django 4.1.6 on 2023-02-10 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0019_feedback"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comments", old_name="object_type", new_name="obj_type",
        ),
    ]
