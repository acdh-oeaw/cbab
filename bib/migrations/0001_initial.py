# Generated by Django 5.0.6 on 2024-06-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "zoterokey",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("item_type", models.CharField(blank=True, max_length=100, null=True)),
                ("author", models.CharField(blank=True, max_length=100, null=True)),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "publication_title",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "short_title",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("publication_year", models.IntegerField(blank=True, null=True)),
                ("place", models.CharField(blank=True, max_length=100, null=True)),
                ("isbn", models.CharField(blank=True, max_length=100, null=True)),
                ("issn", models.CharField(blank=True, max_length=100, null=True)),
                ("doi", models.CharField(blank=True, max_length=100, null=True)),
                ("url", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
