# Generated by Django 5.0.6 on 2024-06-07 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bib", "0001_initial"),
        ("places", "0001_initial"),
        ("vocabs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BurialSite",
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
                        blank=True,
                        help_text="Please provide helptext",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "alternative_name",
                    models.CharField(
                        blank=True, help_text="helptext", max_length=255, null=True
                    ),
                ),
                (
                    "exact_location",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "lat",
                    models.FloatField(blank=True, null=True, verbose_name="latitude"),
                ),
                (
                    "lng",
                    models.FloatField(blank=True, null=True, verbose_name="longitude"),
                ),
                (
                    "excavation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("fully excavated", "fully excavated"),
                            ("partly excavated", "partly excavated"),
                        ],
                        help_text="helptext",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "disturbance",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "total_graves",
                    models.CharField(
                        blank=True,
                        help_text="Total number of excavated graves",
                        max_length=255,
                        null=True,
                        verbose_name="Total number of excavated graves",
                    ),
                ),
                (
                    "absolute_dating",
                    models.CharField(
                        blank=True,
                        help_text="Please provide helptext",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "location_of_archaeological_material_and_contact_information",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "dating",
                    models.ManyToManyField(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/4' target='_blank'>See Dating Concept Schema</a>",
                        related_name="skos_dating",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "distance_to_next_settlement",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/2' target='_blank'>See Distance to next settlement Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_distance_to_next_settlement",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="places.place",
                    ),
                ),
                (
                    "reference",
                    models.ManyToManyField(
                        blank=True, help_text="Please provide helptext", to="bib.book"
                    ),
                ),
                (
                    "topography",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/1' target='_blank'>See Topography Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_topography",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "type_of_burial_site",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/3' target='_blank'>See Type of Burial site Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_type_of_burial_site",
                        to="vocabs.skosconcept",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BurialGroup",
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
                    "burial_group_id",
                    models.CharField(
                        blank=True,
                        help_text="helptext",
                        max_length=255,
                        null=True,
                        verbose_name="Burial group number",
                    ),
                ),
                ("name", models.TextField(blank=True, help_text="helptext", null=True)),
                (
                    "length",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "width",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "diameter",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "height",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "burial_group_type",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/5' target='_blank'>See Burial group type Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_type_of_burial_group",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/6' target='_blank'>See Material Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_material_burialgroup",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "burial_site",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burialsite",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Burial",
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
                    "burial_id",
                    models.CharField(
                        blank=True,
                        help_text="helptext",
                        max_length=255,
                        null=True,
                        verbose_name="Burial number",
                    ),
                ),
                (
                    "C14_dendro",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                        verbose_name="Absolute dating (C14/Dendro)",
                    ),
                ),
                (
                    "absolute_age",
                    models.CharField(
                        blank=True, help_text="helptext", max_length=255, null=True
                    ),
                ),
                (
                    "secondary_burial",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "secondary_burial_text",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "displaced",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "displaced_text",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "extraordinary_burial",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "extraordinary_burial_text",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "inhumation_burial_type",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "bi_ritual_burial_type",
                    models.TextField(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        verbose_name="Bi-ritual burial type",
                    ),
                ),
                (
                    "cover",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "length",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "width",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "diameter",
                    models.CharField(
                        blank=True, help_text="cm", max_length=255, null=True
                    ),
                ),
                (
                    "height",
                    models.CharField(
                        blank=True,
                        help_text="cm",
                        max_length=255,
                        null=True,
                        verbose_name="Depth",
                    ),
                ),
                (
                    "intentionally_deposited",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "post_holes",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "surface_identification_mark",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "erdgraebchen",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "other_features",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "arrangement",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/9' target='_blank'>See Burial arrangement Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_burial_arrangement",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "burial_type",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/7' target='_blank'>See Burial type Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_burial_type",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "construction",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/8' target='_blank'>See Burial construction Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_burial_construction",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "cover_type",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/10' target='_blank'>See Cover type Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_type_of_burial_cover",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "filling",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/27' target='_blank'>See Burial filling type Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_filling",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "filling_objects",
                    models.ManyToManyField(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/26' target='_blank'>See Burial filling objects Concept Schema</a>",
                        related_name="skos_filling_object",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "grave_pit_form",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/11' target='_blank'>See Grave pit form Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_form_of_the_grave_pit",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "grave_pit_orientation",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/12' target='_blank'>See Grave pit orientation Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_orientation_of_the_grave_pit",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "burial_group",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burialgroup",
                    ),
                ),
                (
                    "burial_site",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burialsite",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Urn",
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
                    "urn_type",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "variation",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "urn_id",
                    models.TextField(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        verbose_name="Urn Inventory Number",
                    ),
                ),
                (
                    "urncover_exists",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                        verbose_name="Urn Cover",
                    ),
                ),
                (
                    "basic_shape",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/13' target='_blank'>See Basic shape of urn Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_basic_shape_of_urn",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "burial",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burial",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GraveGoodOther",
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
                    "amount_countable",
                    models.IntegerField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "comment",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "secondary_depostition",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "food",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "other_organic_grave_good",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "other_organic_grave_good_text",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "burial",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burial",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_gravegoodother_position",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "urn",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.urn",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GraveGood",
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
                    "amount_countable",
                    models.IntegerField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "comment",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "secondary_depostition",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "burial",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burial",
                    ),
                ),
                (
                    "condition",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/16' target='_blank'>See Condition Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_condition",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/6' target='_blank'>See Material Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_material",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/28' target='_blank'>See Grave good object Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_name_gravegood",
                        to="vocabs.skosconcept",
                        verbose_name="Type",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_gravegood_position",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "urn",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.urn",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DeadBodyRemains",
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
                    "amount_countable",
                    models.IntegerField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "comment",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "secondary_depostition",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "weight",
                    models.TextField(blank=True, help_text="in gram", null=True),
                ),
                (
                    "pathology",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "total_weight",
                    models.TextField(
                        blank=True,
                        help_text="in gram",
                        null=True,
                        verbose_name="Total weight of Human Remains",
                    ),
                ),
                (
                    "age",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/23' target='_blank'>See Age Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_age",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "burial",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burial",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/24' target='_blank'>See Gender Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_gender",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_deadbodyremains_position",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "temperature",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/25' target='_blank'>See Cremation temperature Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_temperature",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "urn",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.urn",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AnimalRemains",
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
                    "amount_countable",
                    models.IntegerField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "comment",
                    models.TextField(blank=True, help_text="helptext", null=True),
                ),
                (
                    "secondary_depostition",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        blank=True, help_text="helptext", max_length=255, null=True
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        blank=True, help_text="helptext", max_length=255, null=True
                    ),
                ),
                (
                    "weight",
                    models.CharField(
                        blank=True, help_text="helptext", max_length=255, null=True
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_animalsremains_position",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "species",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/29' target='_blank'>See Species Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_species",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "burial",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.burial",
                    ),
                ),
                (
                    "urn",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.urn",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UrnCover",
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
                    "upside_down",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "fragment",
                    models.BooleanField(
                        blank=True,
                        choices=[(None, "Unknown"), (True, "Yes"), (False, "No")],
                        null=True,
                    ),
                ),
                (
                    "cover_id",
                    models.TextField(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        verbose_name="Urn cover inventory number",
                    ),
                ),
                (
                    "basic_shape",
                    models.ForeignKey(
                        blank=True,
                        help_text="<a href='/vocabs/scheme/14' target='_blank'>See Basic shape of urn cover Concept Schema</a>",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="skos_basic_shape_of_urn_cover",
                        to="vocabs.skosconcept",
                    ),
                ),
                (
                    "urn",
                    models.ForeignKey(
                        blank=True,
                        help_text="helptext",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="burials.urn",
                    ),
                ),
            ],
        ),
    ]
