# Generated by Django 5.2 on 2025-05-04 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("tipo", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Remedio",
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
                ("nome", models.CharField(max_length=60)),
                ("marca", models.CharField(max_length=40)),
                ("quantidade", models.FloatField()),
                ("preco_compra", models.FloatField()),
                (
                    "categoria",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="estoque.categoria",
                    ),
                ),
            ],
        ),
    ]
