# Generated by Django 5.0.1 on 2024-01-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("billboards", "0002_billboard_booked"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="billboard",
            name="available_date_from",
        ),
        migrations.RemoveField(
            model_name="billboard",
            name="available_date_to",
        ),
        migrations.RemoveField(
            model_name="billboard",
            name="target_audience_from",
        ),
        migrations.RemoveField(
            model_name="billboard",
            name="target_audience_to",
        ),
        migrations.AddField(
            model_name="billboard",
            name="target_audience",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]