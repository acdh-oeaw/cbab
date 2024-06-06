# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from vocabs.models import SkosConcept
from places.models import Place
from bib.models import Book

FULLYPARTLYEXCAVATED = (
    ("fully excavated", "fully excavated"),
    ("partly excavated", "partly excavated"),
)

BOOLEAN_CHOICES = ((None, "Unknown"), (True, "Yes"), (False, "No"))


class BurialSite(models.Model):
    name = models.CharField(
        max_length=255, blank=True, null=True, help_text="Please provide helptext"
    )
    alternative_name = models.CharField(
        max_length=255, blank=True, null=True, help_text="helptext"
    )
    location = models.ForeignKey(Place, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext")
    topography = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/1' target='_blank'>See Topography Concept Schema</a>",
        related_name="skos_topography",
    )
    exact_location = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    lat = models.FloatField(blank=True, null=True, verbose_name="latitude")
    lng = models.FloatField(blank=True, null=True, verbose_name="longitude")
    excavation = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=FULLYPARTLYEXCAVATED,
        help_text="helptext",
    )
    distance_to_next_settlement = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/2' target='_blank'>See Distance to next settlement Concept Schema</a>",
        related_name="skos_distance_to_next_settlement",
    )
    type_of_burial_site = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/3' target='_blank'>See Type of Burial site Concept Schema</a>",
        related_name="skos_type_of_burial_site",
    )
    disturbance = models.TextField(blank=True, null=True, help_text="helptext")
    total_graves = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Total number of excavated graves",
        null=True,
        help_text="Total number of excavated graves",
    )
    dating = models.ManyToManyField(
        SkosConcept,
        blank=True,
        help_text="<a href='/vocabs/scheme/4' target='_blank'>See Dating Concept Schema</a>",
        related_name="skos_dating",
    )
    absolute_dating = models.CharField(
        max_length=255, blank=True, null=True, help_text="Please provide helptext"
    )
    location_of_archaeological_material_and_contact_information = models.TextField(
        blank=True, null=True, help_text="helptext"
    )
    reference = models.ManyToManyField(
        Book, blank=True, help_text="Please provide helptext"
    )

    def __str__(self):
        return "BurialSite: {}".format(self.name)

    def get_absolute_url(self):
        return reverse("burials:burialsite_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class BurialGroup(models.Model):
    burial_site = models.ForeignKey(
        BurialSite, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext"
    )
    burial_group_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="helptext",
        verbose_name="Burial group number",
    )
    name = models.TextField(blank=True, null=True, help_text="helptext")
    burial_group_type = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/5' target='_blank'>See Burial group type Concept Schema</a>",
        related_name="skos_type_of_burial_group",
    )
    material = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/6' target='_blank'>See Material Concept Schema</a>",
        related_name="skos_material_burialgroup",
    )
    length = models.CharField(max_length=255, blank=True, null=True, help_text="cm")
    width = models.CharField(max_length=255, blank=True, null=True, help_text="cm")
    diameter = models.CharField(max_length=255, blank=True, null=True, help_text="cm")
    height = models.CharField(max_length=255, blank=True, null=True, help_text="cm")

    def __str__(self):
        return "{} | BurialGroup: {}".format(self.burial_site, self.burial_group_id)

    def get_absolute_url(self):
        return reverse("burials:burialgroup_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class Burial(models.Model):
    burial_site = models.ForeignKey(
        BurialSite, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext"
    )
    burial_group = models.ForeignKey(
        BurialGroup, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext"
    )
    burial_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="helptext",
        verbose_name="Burial number",
    )
    burial_type = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/7' target='_blank'>See Burial type Concept Schema</a>",
        related_name="skos_burial_type",
    )
    C14_dendro = models.BooleanField(null=True, blank=True,
        verbose_name="Absolute dating (C14/Dendro)", choices=BOOLEAN_CHOICES
    )
    absolute_age = models.CharField(
        max_length=255, blank=True, null=True, help_text="helptext"
    )
    secondary_burial = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    secondary_burial_text = models.TextField(
        blank=True, null=True, help_text="helptext"
    )
    displaced = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    displaced_text = models.TextField(blank=True, null=True, help_text="helptext")
    extraordinary_burial = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    extraordinary_burial_text = models.TextField(
        blank=True, null=True, help_text="helptext"
    )
    inhumation_burial_type = models.TextField(
        blank=True, null=True, help_text="helptext"
    )
    bi_ritual_burial_type = models.TextField(
        blank=True,
        null=True,
        help_text="helptext",
        verbose_name="Bi-ritual burial type",
    )
    construction = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/8' target='_blank'>See Burial construction Concept Schema</a>",
        related_name="skos_burial_construction",
    )
    arrangement = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/9' target='_blank'>See Burial arrangement Concept Schema</a>",
        related_name="skos_burial_arrangement",
    )
    cover = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    cover_type = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/10' target='_blank'>See Cover type Concept Schema</a>",
        related_name="skos_type_of_burial_cover",
    )
    grave_pit_form = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/11' target='_blank'>See Grave pit form Concept Schema</a>",
        related_name="skos_form_of_the_grave_pit",
    )
    grave_pit_orientation = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/12' target='_blank'>See Grave pit orientation Concept Schema</a>",
        related_name="skos_orientation_of_the_grave_pit",
    )
    length = models.CharField(max_length=255, blank=True, null=True, help_text="cm")
    width = models.CharField(max_length=255, blank=True, null=True, help_text="cm")
    diameter = models.CharField(max_length=255, blank=True, null=True, help_text="cm")
    height = models.CharField(
        max_length=255, blank=True, null=True, help_text="cm", verbose_name="Depth"
    )
    filling_objects = models.ManyToManyField(
        SkosConcept,
        blank=True,
        help_text="<a href='/vocabs/scheme/26' target='_blank'>See Burial filling objects Concept Schema</a>",
        related_name="skos_filling_object",
    )
    intentionally_deposited = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    filling = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/27' target='_blank'>See Burial filling type Concept Schema</a>",
        related_name="skos_filling",
    )
    post_holes = models.TextField(blank=True, null=True, help_text="helptext")
    surface_identification_mark = models.TextField(
        blank=True, null=True, help_text="helptext"
    )
    erdgraebchen = models.TextField(blank=True, null=True, help_text="helptext")
    other_features = models.TextField(blank=True, null=True, help_text="helptext")

    def __str__(self):
        if self.burial_group is None:
            return "{} | Burial: {}".format(self.burial_site, self.burial_id)
        else:
            return " {} | Burial: {}".format(self.burial_group, self.burial_id)

    def get_absolute_url(self):
        return reverse("burials:burial_detail", kwargs={"pk": self.id})

    @property
    def related_gravegoods(self):
        goods = []
        for x in GraveGood.objects.filter(burial=self.id):
            try:
                goods.append(
                    [
                        x.name.skos_broader.all()[0].pref_label,
                        x.name.pref_label,
                        x.amount_countable,
                    ]
                )
            except: # noqa
                goods.append([x])
        return goods

    @property
    def amount_related_gravegoods(self):
        goods = []
        for x in GraveGood.objects.filter(burial=self.id):
            if x.amount_countable:
                goods.append(x.amount_countable)
        return sum(goods)

    @property
    def amount_related_deadbodyremains(self):
        deadbodyremains = []
        for x in DeadBodyRemains.objects.filter(burial=self.id):
            if x.amount_countable:
                deadbodyremains.append(x.amount_countable)
        return sum(deadbodyremains)

    @property
    def amount_related_organic(self):
        organic = []
        for x in AnimalRemains.objects.filter(burial=self.id):
            if x.amount_countable:
                organic.append(x.amount_countable)
        return sum(organic)

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class Urn(models.Model):
    burial = models.ForeignKey(Burial, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext")
    basic_shape = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/13' target='_blank'>See Basic shape of urn Concept Schema</a>",
        related_name="skos_basic_shape_of_urn",
    )
    urn_type = models.TextField(blank=True, null=True, help_text="helptext")
    variation = models.TextField(blank=True, null=True, help_text="helptext")
    urn_id = models.TextField(
        blank=True, null=True, help_text="helptext", verbose_name="Urn Inventory Number"
    )
    urncover_exists = models.BooleanField(null=True, blank=True,
        verbose_name="Urn Cover", choices=BOOLEAN_CHOICES
    )

    def __str__(self):
        return "{}- ID {} {}".format(self.urn_id, self.id, self.burial)

    def get_absolute_url(self):
        return reverse("burials:urn_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name

    @property
    def related_gravegoods(self):
        goods = []
        for x in GraveGood.objects.filter(urn=self.id):
            goods.append(
                [
                    x.name.skos_broader.all()[0].pref_label,
                    x.name.pref_label,
                    x.amount_countable,
                ]
            )
        return goods


class UrnCover(models.Model):
    basic_shape = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/14' target='_blank'>See Basic shape of urn cover Concept Schema</a>",
        related_name="skos_basic_shape_of_urn_cover",
    )
    upside_down = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    fragment = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    cover_id = models.TextField(
        blank=True,
        null=True,
        help_text="helptext",
        verbose_name="Urn cover inventory number",
    )
    urn = models.ForeignKey(Urn, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext")

    def __str__(self):
        return "{}-{}-{}".format(self.urn, self.cover_id, self.id)

    def get_absolute_url(self):
        return reverse("burials:urncover_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class CrematedRemainsBaseClass(models.Model):
    """An abstract class for Grave Goods and living remains"""

    burial = models.ForeignKey(
        Burial,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="helptext"
    )
    urn = models.ForeignKey(Urn, on_delete=models.SET_NULL, blank=True, null=True, help_text="helptext")
    amount_countable = models.IntegerField(null=True, blank=True, help_text="helptext")
    comment = models.TextField(blank=True, null=True, help_text="helptext")
    secondary_depostition = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)

    class Meta:
        abstract = True


class GraveGood(CrematedRemainsBaseClass):
    name = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/28' target='_blank'>See Grave good object Concept Schema</a>",
        related_name="skos_name_gravegood",
        verbose_name="Type",
    )
    material = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/6' target='_blank'>See Material Concept Schema</a>",
        related_name="skos_material",
    )
    condition = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/16' target='_blank'>See Condition Concept Schema</a>",
        related_name="skos_condition",
    )
    position = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
        related_name="skos_gravegood_position",
    )

    def __str__(self):
        return "type: {} | material: {} | amount: {}".format(
            self.name, self.material, self.amount_countable
        )

    def get_absolute_url(self):
        return reverse("burials:gravegood_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class GraveGoodOther(CrematedRemainsBaseClass):
    food = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    other_organic_grave_good = models.BooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)
    other_organic_grave_good_text = models.TextField(
        blank=True, null=True, help_text="helptext"
    )
    position = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
        related_name="skos_gravegoodother_position",
    )

    def __str__(self):
        if self.food is True and (
            self.other_organic_grave_good is False
            or self.other_organic_grave_good is None
        ):
            return "food ID {}".format(self.id)
        elif self.other_organic_grave_good is True and (
            self.food is False or self.food is None
        ):
            return "other ID {}".format(self.id)
        elif self.other_organic_grave_good is True and self.food is True:
            return "food and other ID {}".format(self.id)
        else:
            return "ID {}".format(self.id)

    def get_absolute_url(self):
        return reverse("burials:gravegoodother_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class DeadBodyRemains(CrematedRemainsBaseClass):
    age = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/23' target='_blank'>See Age Concept Schema</a>",
        related_name="skos_age",
    )
    gender = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/24' target='_blank'>See Gender Concept Schema</a>",
        related_name="skos_gender",
    )
    temperature = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/25' target='_blank'>See Cremation temperature Concept Schema</a>",
        related_name="skos_temperature",
    )
    weight = models.TextField(blank=True, null=True, help_text="in gram")
    pathology = models.TextField(blank=True, null=True, help_text="helptext")
    total_weight = models.TextField(
        blank=True,
        null=True,
        help_text="in gram",
        verbose_name="Total weight of Human Remains",
    )
    position = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
        related_name="skos_deadbodyremains_position",
    )

    def __str__(self):
        return "age: {} | gender: {} | amount: {}".format(
            self.age, self.gender, self.amount_countable
        )

    def get_absolute_url(self):
        return reverse("burials:deadbodyremains_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class AnimalRemains(CrematedRemainsBaseClass):
    species = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/29' target='_blank'>See Species Concept Schema</a>",
        related_name="skos_species",
    )
    age = models.CharField(max_length=255, blank=True, null=True, help_text="helptext")
    sex = models.CharField(max_length=255, blank=True, null=True, help_text="helptext")
    weight = models.CharField(
        max_length=255, blank=True, null=True, help_text="helptext"
    )
    position = models.ForeignKey(
        SkosConcept,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="<a href='/vocabs/scheme/17' target='_blank'>See Position Concept Schema</a>",
        related_name="skos_animalsremains_position",
    )

    def __str__(self):
        return "species: {} | age: {} | sex: {} | amount: {}".format(
            self.species, self.age, self.sex, self.amount_countable
        )

    def get_absolute_url(self):
        return reverse("burials:animalremains_detail", kwargs={"pk": self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name
