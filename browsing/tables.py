import django_tables2 as tables
from django_tables2.utils import A
from burials.models import (
    BurialSite,
    BurialGroup,
    Burial,
    Urn,
    UrnCover,
    GraveGood,
    GraveGoodOther,
    DeadBodyRemains,
    AnimalRemains,
)


class BurialSiteTable(tables.Table):
    id = tables.LinkColumn(
        "burials:burialsite_detail", args=[A("pk")], verbose_name="cbab-id"
    )
    name = tables.LinkColumn("burials:burialsite_detail", args=[A("pk")])

    class Meta:
        model = BurialSite
        fields = ["id", "name", "type_of_burial_site"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BurialGroupTable(tables.Table):
    db_id = tables.LinkColumn(
        "burials:burialgroup_detail", args=[A("pk")], accessor="id"
    )
    burial_group_id = tables.LinkColumn("burials:burialgroup_detail", args=[A("pk")])
    burial_site = tables.Column()

    class Meta:
        model = BurialGroup
        fields = ["db_id", "burial_group_id", "burial_group_type"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BurialTable(tables.Table):
    burial = tables.TemplateColumn(
        """<a href="{% url 'burials:burial_detail' pk=record.id %}">{{ record }}</a>""",
        order_by="burial_site",
    )
    burial_site = tables.RelatedLinkColumn()
    burial_group = tables.RelatedLinkColumn()

    class Meta:
        model = Burial
        fields = ["burial", "burial_site", "burial_group"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class UrnCoverTable(tables.Table):
    db_id = tables.LinkColumn("burials:urncover_detail", args=[A("pk")], accessor="id")
    cover_id = tables.LinkColumn("burials:urncover_detail", args=[A("pk")])

    class Meta:
        model = UrnCover
        fields = ["db_id", "cover_id", "basic_shape"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class UrnTable(tables.Table):
    db_id = tables.LinkColumn("burials:urn_detail", args=[A("pk")], accessor="id")
    urn_id = tables.LinkColumn("burials:urn_detail", args=[A("pk")])
    burial = tables.RelatedLinkColumn()

    class Meta:
        model = Urn
        fields = ["db_id", "urn_id", "basic_shape"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class GraveGoodTable(tables.Table):
    db_id = tables.LinkColumn("burials:gravegood_detail", args=[A("pk")], accessor="id")
    name = tables.LinkColumn("burials:gravegood_detail", args=[A("pk")])
    burial = tables.RelatedLinkColumn()

    class Meta:
        model = GraveGood
        fields = ["db_id", "name", "material"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class GraveGoodOtherTable(tables.Table):
    db_id = tables.LinkColumn(
        "burials:gravegoodother_detail", args=[A("pk")], accessor="id"
    )
    burial = tables.RelatedLinkColumn()

    class Meta:
        model = GraveGoodOther
        fields = ["db_id", "burial"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class DeadBodyRemainsTable(tables.Table):
    db_id = tables.LinkColumn(
        "burials:deadbodyremains_detail", args=[A("pk")], accessor="id"
    )
    burial = tables.RelatedLinkColumn()

    class Meta:
        model = DeadBodyRemains
        fields = ["db_id", "age"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class AnimalRemainsTable(tables.Table):
    db_id = tables.LinkColumn(
        "burials:animalremains_detail", args=[A("pk")], accessor="id"
    )
    burial = tables.RelatedLinkColumn()

    class Meta:
        model = AnimalRemains
        fields = ["db_id", "species"]
        attrs = {"class": "table table-hover table-striped table-condensed"}


class FillingObjectTable(tables.Table):
    db_id = tables.LinkColumn(
        "burials:burialfilling_detail", args=[A("pk")], accessor="id"
    )
    burial = tables.RelatedLinkColumn()

    class Meta:
        model = AnimalRemains
        fields = ["db_id", "filling_objects", "burial"]
        attrs = {"class": "table table-hover table-striped table-condensed"}
