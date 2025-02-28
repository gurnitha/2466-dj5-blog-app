# Generated by Django 5.0.4 on 2024-06-25 00:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
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
                ("platform", models.CharField(max_length=25)),
                ("link", models.URLField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
