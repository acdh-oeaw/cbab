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

BOOLEAN_CHOICES = (
    (None, "Unknown"),
    (True, "Yes"),
    (False, "No")
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
    exact_location = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    lat = models.FloatField(blank=True, null=True, verbose_name='latitude')
    lng = models.FloatField(blank=True, null=True, verbose_name='longitude')
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
    absolute_dating = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Please provide helptext")
    location_of_archaeological_material_and_contact_information = models.TextField(
        blank=True, null=True, help_text="helptext")
    reference = models.ManyToManyField(
        Book, blank=True, help_text="Please provide helptext")

    def __str__(self):
        return "BurialSite: {}".format(self.name)

    def get_absolute_url(self):
        return reverse('burials:burialsite_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class BurialGroup(models.Model):
    burial_site = models.ForeignKey(
        BurialSite, blank=True, null=True,
        help_text="helptext")
    burial_group_id = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext", verbose_name="Burial group number")
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
        help_text="cm")
    width = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="cm")
    diameter = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="cm")
    height = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="cm")

    def __str__(self):
        return "{} | BurialGroup: {}".format(self.burial_site, self.burial_group_id)

    def get_absolute_url(self):
        return reverse('burials:burialgroup_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class Burial(models.Model):
    burial_site = models.ForeignKey(
        BurialSite, blank=True, null=True, help_text="helptext")
    burial_group = models.ForeignKey(
        BurialGroup, blank=True, null=True, help_text="helptext")
    burial_id = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext", verbose_name="Burial number")
    burial_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_burial_type")
    C14_dendro = models.NullBooleanField(verbose_name="Absolute dating (C14/Dendro)",
        choices=BOOLEAN_CHOICES)
    absolute_age = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="helptext")
    secondary_burial = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    secondary_burial_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    displaced = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    displaced_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    extraordinary_burial = models.NullBooleanField(choices=BOOLEAN_CHOICES)
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
    cover = models.NullBooleanField(choices=BOOLEAN_CHOICES)
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
        help_text="cm")
    width = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="cm")
    diameter = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="cm")
    height = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="cm", verbose_name="Depth")
    filling_objects = models.ManyToManyField(
        SkosConcept, blank=True,
        help_text="helptext", related_name="skos_filling_object")
    intentionally_deposited = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    filling = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_filling")
    post_holes = models.TextField(
        blank=True, null=True, help_text="helptext")
    surface_identification_mark = models.TextField(
        blank=True, null=True, help_text="helptext")
    erdgraebchen = models.TextField(
        blank=True, null=True,
        help_text="helptext")
    other_features = models.TextField(
        blank=True, null=True, help_text="helptext")

    def __str__(self):
        if self.burial_group is None:
            return "{} | Burial: {}".format(self.burial_site, self.burial_id)
        else:
            return " {} | Burial: {}".format(
                self.burial_group, self.burial_id
            )

    def get_absolute_url(self):
        return reverse('burials:burial_detail', kwargs={'pk': self.id})

    @property
    def related_gravegoods(self):
        goods = []
        for x in GraveGood.objects.filter(burial=self.id):
            try:
                goods.append(
                    [x.name.skos_broader.all()[0].pref_label, x.name.pref_label, x.amount_countable]
                    )
            except:
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


# class FillingObject(models.Model):
#     burial = models.ForeignKey(Burial, blank=True, null=True, help_text="helptext")
#     filling_objects = models.ForeignKey(
#         SkosConcept, blank=True, null=True,
#         help_text="helptext", related_name="skos_filling_object")
#     amount_countable = models.IntegerField(null=True, blank=True, help_text="helptext")
#     intentionally_deposited = models.NullBooleanField()
#     burial_filling_comment = models.TextField(
#         blank=True, null=True, help_text="helptext", verbose_name="Comment")
#
#     def __str__(self):
#         return "type: {} | amount: {}".format(self.filling_objects, self.amount_countable)
#
#     def get_absolute_url(self):
#         return reverse('burials:burialfilling_detail', kwargs={'pk': self.id})
#
#     def get_classname(self):
#         """Returns the name of the class as lowercase string"""
#         class_name = str(self.__class__.__name__).lower()
#         return class_name


class Urn(models.Model):
    burial = models.ForeignKey(
        Burial,
        blank=True, null=True,
        help_text="helptext")
    basic_shape = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_basic_shape_of_urn"
    )
    urn_type = models.TextField(
        blank=True, null=True, help_text="helptext")
    variation = models.TextField(
        blank=True, null=True, help_text="helptext")
    urn_id = models.TextField(
        blank=True, null=True, help_text="helptext", verbose_name="Urn Inventory Number")

    urncover_exists = models.NullBooleanField(verbose_name="Urn Cover",
        choices=BOOLEAN_CHOICES)

    def __str__(self):
        return "{}-{} {}".format(self.urn_id, self.id, self.burial)

    def get_absolute_url(self):
        return reverse('burials:urn_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name

    @property
    def related_gravegoods(self):
        goods = []
        for x in GraveGood.objects.filter(urn=self.id):
            goods.append(
                [x.name.skos_broader.all()[0].pref_label, x.name.pref_label, x.amount_countable]
            )
        return goods


class UrnCover(models.Model):
    basic_shape = models.ForeignKey(
        SkosConcept, blank=True, null=True,
        help_text="helptext", related_name="skos_basic_shape_of_urn_cover"
    )
    upside_down = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    fragment = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    cover_id = models.TextField(
        blank=True, null=True, help_text="helptext", verbose_name="Urn cover inventory number")
    urn = models.ForeignKey(Urn, blank=True, null=True, help_text="helptext")

    def __str__(self):
        return "{}-{}-{}".format(self.urn, self.cover_id, self.id)

    def get_absolute_url(self):
        return reverse('burials:urncover_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class CrematedRemainsBaseClass(models.Model):
    """An abstract class for Grave Goods and living remains"""
    burial = models.ForeignKey(Burial, blank=True, null=True, help_text="helptext")
    urn = models.ForeignKey(Urn, blank=True, null=True, help_text="helptext")
    amount_countable = models.IntegerField(null=True, blank=True, help_text="helptext")
    comment = models.TextField(blank=True, null=True, help_text="helptext")
    secondary_depostition = models.NullBooleanField(choices=BOOLEAN_CHOICES)

    class Meta:
        abstract = True


class GraveGood(CrematedRemainsBaseClass):
    name = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_name_gravegood", verbose_name="Type")
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
        return "type: {} | material: {} | amount: {}".format(
            self.name, self.material, self.amount_countable
        )

    def get_absolute_url(self):
        return reverse('burials:gravegood_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class GraveGoodOther(CrematedRemainsBaseClass):
    food = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    other_organic_grave_good = models.NullBooleanField(choices=BOOLEAN_CHOICES)
    other_organic_grave_good_text = models.TextField(
        blank=True, null=True, help_text="helptext")
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_gravegoodother_position")

    def __str__(self):
        return "food: {} | other: {} | text: {}".format(
            self.food, self.other_organic_grave_good, self.other_organic_grave_good_text
        )

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
        blank=True, null=True, help_text="in gram")
    pathology = models.TextField(
        blank=True, null=True, help_text="helptext")
    total_weight = models.TextField(
        blank=True, null=True, help_text="in gram", verbose_name="Total weight of Human Remains")
    position = models.ForeignKey(
        SkosConcept, blank=True, null=True, help_text="helptext",
        related_name="skos_deadbodyremains_position")

    def __str__(self):
        return "age: {} | gender: {} | amount: {}".format(
            self.age, self.gender, self.amount_countable)

    def get_absolute_url(self):
        return reverse('burials:deadbodyremains_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class AnimalRemains(CrematedRemainsBaseClass):
    species = models.ForeignKey(
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
        return "species: {} | age: {} | sex: {} | amount: {}".format(
            self.species, self.age, self.sex, self.amount_countable
        )

    def get_absolute_url(self):
        return reverse('burials:animalremains_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name
