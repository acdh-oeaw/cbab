# Generated by Django 5.0.6 on 2024-06-07 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AlternativeName",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, help_text="Alternative Name", max_length=250
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Province",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, help_text="Normalized name", max_length=250
                    ),
                ),
                (
                    "geonames_id",
                    models.CharField(blank=True, help_text="GND-ID", max_length=50),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True, decimal_places=12, max_digits=20, null=True
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        blank=True, decimal_places=12, max_digits=20, null=True
                    ),
                ),
                (
                    "place_type",
                    models.CharField(
                        blank=True,
                        choices=[("city", "city"), ("country", "country")],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "alternative_name",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Alternative names",
                        max_length=250,
                        to="places.alternativename",
                    ),
                ),
                (
                    "part_of",
                    models.ForeignKey(
                        blank=True,
                        help_text="A place (country) this place is part of.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="places.place",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="places.province",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=250)),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="places.country",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="province",
            name="region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="places.region",
            ),
        ),
    ]
