# Generated by Django 4.2.4 on 2024-01-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
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
                ("code", models.CharField(max_length=10, verbose_name="Код валюты")),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Наименование валюты"),
                ),
                (
                    "rate",
                    models.DecimalField(
                        decimal_places=4, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                ("date", models.DateField(verbose_name="Дата")),
            ],
            options={
                "verbose_name": "Курс валюты",
                "verbose_name_plural": "Курсы валют",
                "ordering": ["-date"],
            },
        ),
    ]
