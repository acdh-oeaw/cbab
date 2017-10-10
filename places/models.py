from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=250, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.country, self.name)


class Province(models.Model):
    name = models.CharField(max_length=250, blank=True)
    region = models.ForeignKey(Region, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.region, self.name)


class AlternativeName(models.Model):
    name = models.CharField(max_length=250, blank=True, help_text="Alternative Name")

    def __str__(self):
        return self.name


class Place(models.Model):
    PLACE_TYPES = (
        ("city", "city"),
        ("country", "country")
    )

    """Holds information about places."""
    name = models.CharField(
        max_length=250, blank=True, help_text="Normalized name"
    )
    province = models.ForeignKey(Province, blank=True, null=True)
    alternative_name = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text="Alternative names"
    )
    geonames_id = models.CharField(
        max_length=50, blank=True,
        help_text="GND-ID"
    )
    lat = models.DecimalField(
        max_digits=20, decimal_places=12,
        blank=True, null=True
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    part_of = models.ForeignKey(
        "Place", null=True, blank=True, help_text="A place (country) this place is part of."
    )
    place_type = models.CharField(choices=PLACE_TYPES, null=True, blank=True, max_length=50)

    class Meta:
        ordering  = ['name']

    def __str__(self):
        return "{} ({})".format(self.name, self.province)
