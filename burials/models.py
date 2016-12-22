# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept
from places.models import Place
from bib.models import Book

YESNO = (
    ("yes", "yes"),
    ("no", "no")
)

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
    geographical_coordinate_reference_system = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_geographical_coordinate_reference_system")
    topography = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_topography")
    exact_location = models.CharField(
        max_length=5, blank=True,
        null=True, choices=YESNO, help_text="helptext")
    excavation = models.CharField(
        max_length=5, blank=True,
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
        SkosConcept, blank=True, help_text="helptext", related_name="skos_absolute_dating")
    location_of_archaeological_material_and_contact_information = models.TextField(
        blank=True, null=True, help_text="helptext")
    reference = models.ManyToManyField(
        Book, blank=True, help_text="Please provide helptext")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:burialsite_detail', kwargs={'pk': self.id})


class BurialGroup(models.Model):
    burial_group_id = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
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
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:burialgroup_detail', kwargs={'pk': self.id})


class Burial(models.Model):
    burial_group = models.ForeignKey(
        BurialGroup, blank=True, null=True, help_text="helptext")
    burial_site = models.ForeignKey(
        BurialSite, blank=True, null=True, help_text="helptext")
    burial_id = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    C14_dendro = models.CharField(
        max_length=5, blank=True, null=True, choices=YESNO, help_text="helptext",
        verbose_name="Absolute dating (C14/Dendro)")
    absolute_age = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    burial_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_burial_type")
    individuals = models.CharField(
        max_length=5, blank=True, null=True, choices=YESNO,
        help_text="helptext")  # do we need this field if the total number will be calculated?
    secondary_burial = models.CharField(
        max_length=5, blank=True, null=True, choices=YESNO, help_text="helptext")
    secondary_burial_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    displaced = models.CharField(
        max_length=5, blank=True, null=True, choices=YESNO, help_text="helptext")
    displaced_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    extraordinary_burial = models.CharField(
        max_length=5, blank=True, null=True, choices=YESNO, help_text="helptext")
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
    cover = models.CharField(
        max_length=5, blank=True, null=True, choices=YESNO, help_text="helptext")
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

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:burial_detail', kwargs={'pk': self.id})


class UrnCover(models.Model):
    cover_id = models.TextField(blank=True, null=True,           #ask if it is correct name for this property
        help_text="helptext")
    upside_down = models.CharField(max_length=5, blank=True,
        null=True, choices=YESNO, help_text="helptext")
    fragment = models.CharField(max_length=5, blank=True,
        null=True, choices=YESNO, help_text="helptext")
    basic_shape = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name = "skos_basic_shape_of_urn_cover")


    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:urncover_detail', kwargs={'pk':self.id})


class Urn(models.Model):
    burial = models.ForeignKey(Burial,
        blank=True, null=True,
        help_text="helptext")
    basic_shape = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name = "skos_basic_shape_of_urn")
    urn_id = models.TextField(blank=True, null=True,
        help_text="helptext")
    urn_type = models.TextField(blank=True, null=True,              #TYPE is reserved word in django, not clear TYPE OF WHAT ?
        help_text="helptext")
    variation = models.TextField(blank=True, null=True,
        help_text="helptext")
    cover = models.ForeignKey(UrnCover, blank=True,
        null=True, help_text="helptext")    
    # position_of_cremated_remains = models.ForeignKey(SkosConcept,
 #        blank=True, null=True,
 #        help_text="helptext", related_name = "skos_position_of_cremated_remains")
    # position_of_cremated_remains_inside_the_urn_vessel = models.ForeignKey(SkosConcept,
 #        blank=True, null=True,
 #        help_text="helptext", related_name = "skos_position_of_cremated_remains_inside_the_urn_vessel")
    # position_of_cremated_remains_in_the_grave_pit = models.ForeignKey(SkosConcept,
 #        blank=True, null=True,
 #        help_text="helptext", related_name = "skos_position_of_cremated_remains_in_the_grave_pit")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:urn_detail', kwargs={'pk':self.id})


class GraveGood(models.Model):
    burial = models.ForeignKey(Burial,
        blank=True, null=True,
        help_text="helptext")
    name = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name = "skos_name_gravegood")
    material = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name = "skos_material")
    condition = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name = "skos_condition")
    position = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name = "skos_position")
    amount = models.IntegerField(null=True, blank=True,
        help_text="helptext")


    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:gravegood_detail', kwargs={'pk':self.id})


class GraveGoodOther(models.Model):
    burial = models.ForeignKey(Burial,
        blank=True, null=True,
        help_text="helptext")
    food = models.CharField(max_length=5, blank=True,
        null=True, choices=YESNO, help_text="helptext")
    other_organic_grave_good = models.CharField(max_length=5, blank=True,
        null=True, choices=YESNO, help_text="helptext")
    other_organic_grave_good_text = models.CharField(max_length=5, blank=True,
        null=True, choices=YESNO, help_text="helptext")


    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:gravegoodother_detail', kwargs={'pk':self.id})


class DeadBodyRemains(models.Model):
    burial = models.ForeignKey(Burial,
        blank=True, null=True,
        help_text="helptext")
    age = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name="skos_age")
    gender = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name="skos_gender")
    temperature = models.ForeignKey(SkosConcept,
        blank=True, null=True,
        help_text="helptext", related_name="skos_temperature")
    weight = models.TextField(blank=True, null=True,
        help_text="helptext")
    pathology = models.TextField(blank=True, null=True,
        help_text="helptext")
    total_weight = models.TextField(blank=True, null=True,
        help_text="helptext")

    def __str__(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse('burials:deadbodyremains_detail', kwargs={'pk': self.id})
