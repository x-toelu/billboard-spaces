# Generated by Django 5.0.1 on 2024-01-30 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BillboardRequirement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("abia", "Abia"),
                            ("adamawa", "Adamawa"),
                            ("akwa_ibom", "Akwa Ibom"),
                            ("anambra", "Anambra"),
                            ("bauchi", "Bauchi"),
                            ("bayelsa", "Bayelsa"),
                            ("benue", "Benue"),
                            ("borno", "Borno"),
                            ("cross_river", "Cross River"),
                            ("delta", "Delta"),
                            ("ebonyi", "Ebonyi"),
                            ("edo", "Edo"),
                            ("ekiti", "Ekiti"),
                            ("enugu", "Enugu"),
                            ("gombe", "Gombe"),
                            ("imo", "Imo"),
                            ("jigawa", "Jigawa"),
                            ("kaduna", "Kaduna"),
                            ("kano", "Kano"),
                            ("katsina", "Katsina"),
                            ("kebbi", "Kebbi"),
                            ("kogi", "Kogi"),
                            ("kwara", "Kwara"),
                            ("lagos", "Lagos"),
                            ("nasarawa", "Nasarawa"),
                            ("niger", "Niger"),
                            ("ogun", "Ogun"),
                            ("ondo", "Ondo"),
                            ("osun", "Osun"),
                            ("oyo", "Oyo"),
                            ("plateau", "Plateau"),
                            ("rivers", "Rivers"),
                            ("sokoto", "Sokoto"),
                            ("taraba", "Taraba"),
                            ("yobe", "Yobe"),
                            ("zamfara", "Zamfara"),
                            ("fct_abuja", "FCT (Abuja)"),
                        ],
                        max_length=255,
                    ),
                ),
                ("link", models.URLField(max_length=255, null=True)),
                ("document", models.FileField(null=True, upload_to="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="billboard_requirements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
