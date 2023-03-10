# Generated by Django 4.1.6 on 2023-02-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None, help_text='created_at', verbose_name='created_at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, help_text='modified_at', verbose_name='modified_at'),
        ),
    ]
