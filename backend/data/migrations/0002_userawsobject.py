# Generated by Django 4.1.3 on 2022-11-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAwsObject",
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
                ("object", models.CharField(max_length=500)),
            ],
        ),
    ]
