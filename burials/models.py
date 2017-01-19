# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept
from places.models import Place
from bib.models import Book

FULLYPARTLYEXCAVATED = (
    ("fully excavated", "fully excavated"),
    ("partly excavated", "partly excavated")
)


class BurialSite(models.Model):

    name = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Please provide helptext")
    alternative_name = models.CharField(
        max_length=255, blank=True,
        null=True, help_text="helptext")
    location = models.ForeignKey(
        Place, blank=True, null=True, help_text="helptext")
    topography = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_topography")
    exact_location = models.NullBooleanField()
    lng = models.FloatField(blank=True, null=True, verbose_name='longitude')
    lat = models.FloatField(blank=True, null=True, verbose_name='latitude')
    excavation = models.CharField(
        max_length=50, blank=True,
        null=True, choices=FULLYPARTLYEXCAVATED, help_text="helptext")
    distance_to_next_settlement = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_distance_to_next_settlement")
    type_of_burial_site = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_type_of_burial_site")
    disturbance = models.TextField(
        blank=True, null=True, help_text="helptext")
    dating = models.ManyToManyField(
        SkosConcept, blank=True, help_text="helptext", related_name="skos_dating")
    absolute_dating = models.ManyToManyField(
        SkosConcept, blank=True, help_text="helptext", related_name="skos_absolute_dating")  # 7705
    location_of_archaeological_material_and_contact_information = models.TextField(
        blank=True, null=True, help_text="helptext")
    reference = models.ManyToManyField(
        Book, blank=True, help_text="Please provide helptext")

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('burials:burialsite_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class BurialGroup(models.Model):
    burial_group_id = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext", verbose_name="Burial group number")
    burial_site = models.ForeignKey(
        BurialSite, blank=True, null=True,
        help_text="helptext")
    name = models.TextField(
        blank=True, null=True, help_text="helptext")
    burial_group_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_type_of_burial_group")
    material = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_material_burialgroup")
    length = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    width = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    diameter = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    height = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")

    def __str__(self):
        return "{}-{}-{}".format(self.burial_site.name, self.burial_group_id, self.id)

    def get_absolute_url(self):
        return reverse('burials:burialgroup_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class Burial(models.Model):
    burial_group = models.ForeignKey(
        BurialGroup, blank=True, null=True, help_text="helptext")
    burial_site = models.ForeignKey(
        BurialSite, blank=True, null=True, help_text="helptext")
    burial_id = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext", verbose_name="Burial number")
    C14_dendro = models.NullBooleanField(verbose_name="Absolute dating (C14/Dendro)")
    absolute_age = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    burial_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_burial_type")
    secondary_burial = models.NullBooleanField()
    secondary_burial_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    displaced = models.NullBooleanField()
    displaced_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    extraordinary_burial = models.NullBooleanField()
    extraordinary_burial_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    inhumation_burial_type = models.TextField(
        blank=True, null=True, help_text="helptext")
    bi_ritual_burial_type = models.TextField(
        blank=True, null=True, help_text="helptext", verbose_name="Bi-ritual burial type")
    construction = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_burial_construction")
    arrangement = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_burial_arrangement")
    cover = models.NullBooleanField()
    cover_type = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_type_of_burial_cover")
    grave_pit_form = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_form_of_the_grave_pit")
    grave_pit_orientation = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_orientation_of_the_grave_pit")
    length = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    width = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    diameter = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    height = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    post_holes = models.TextField(
        blank=True, null=True, help_text="helptext")
    surface_identification_mark = models.TextField(
        blank=True, null=True, help_text="helptext")
    erdgraebchen = models.TextField(
        blank=True, null=True,  # CHANGE FOR ENGLISH
        help_text="helptext")
    other_features = models.TextField(
        blank=True, null=True, help_text="helptext")
    burial_filling = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_burial_filling")
    objects_in_burial = models.ManyToManyField(
        SkosConcept, blank=True,
        help_text="helptext", related_name="skos_objects_in_burial")
    intentionally_deposited = models.NullBooleanField()
    burial_filling_type = models.TextField(
        blank=True, null=True, help_text="helptext")
    burial_filling_position = models.TextField(
        blank=True, null=True, help_text="helptext")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:burial_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class UrnCover(models.Model):
    cover_id = models.TextField(
        blank=True, null=True, help_text="helptext", verbose_name="Inventory number")
    upside_down = models.NullBooleanField()
    fragment = models.NullBooleanField()
    basic_shape = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_basic_shape_of_urn_cover"
    )

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:urncover_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class Urn(models.Model):
    burial = models.ForeignKey(
        Burial,
        blank=True, null=True,
        help_text="helptext")
    basic_shape = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_basic_shape_of_urn"
    )
    urn_id = models.TextField(
        blank=True, null=True, help_text="helptext", verbose_name="Inventory number")
    urn_type = models.TextField(
        blank=True, null=True, help_text="helptext")
    variation = models.TextField(
        blank=True, null=True, help_text="helptext")
    cover = models.ForeignKey(UrnCover, blank=True, null=True, help_text="helptext")

    def __str__(self):
        return "{}-{}".format(self.urn_id, self.id)

    def get_absolute_url(self):
        return reverse('burials:urn_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class CrematedRemainsBaseClass(models.Model):
    """An abstract class for Grave Goods and living remains"""
    burial = models.ForeignKey(Burial, blank=True, null=True, help_text="helptext")
    urn = models.ForeignKey(Urn, blank=True, null=True, help_text="helptext")
    position_comment = models.TextField(blank=True, null=True, help_text="helptext")
    amount_countable = models.IntegerField(null=True, blank=True, help_text="helptext")
    amount_comment = models.TextField(blank=True, null=True, help_text="helptext")
    secondary_depostition = models.NullBooleanField()

    class Meta:
        abstract = True


class GraveGood(CrematedRemainsBaseClass):
    name = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_name_gravegood")
    material = models.ForeignKey(
        SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name="skos_material")
    condition = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_condition")
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_gravegood_position")

    def __str__(self):
        return "{}-{}".format(self.burial.burial_site.name, self.id)

    def get_absolute_url(self):
        return reverse('burials:gravegood_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class GraveGoodOther(CrematedRemainsBaseClass):
    food = models.NullBooleanField()
    other_organic_grave_good = models.NullBooleanField()
    other_organic_grave_good_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_gravegoodother_position")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:gravegoodother_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class DeadBodyRemains(CrematedRemainsBaseClass):
    age = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext", related_name="skos_age")
    gender = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext", related_name="skos_gender")
    temperature = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_temperature")
    weight = models.TextField(
        blank=True, null=True, help_text="helptext")
    pathology = models.TextField(
        blank=True, null=True, help_text="helptext")
    total_weight = models.TextField(
        blank=True, null=True, help_text="helptext")
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_deadbodyremains_position")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:deadbodyremains_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class AnimalRemains(CrematedRemainsBaseClass):
    species = models.ManyToManyField(
        SkosConcept, blank=True, help_text="helptext", related_name="skos_species")
    age = models.CharField(
        max_length=255, blank=True, null=True, help_text="helptext")
    sex = models.CharField(
        max_length=255, blank=True, null=True, help_text="helptext")
    weight = models.CharField(
        max_length=255, blank=True, null=True, help_text="helptext")
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_animalsremains_position")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:animalremains_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name
