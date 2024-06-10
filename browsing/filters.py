import django_filters
from . import forms
from browsing.forms import *
from burials.models import *
from vocabs.models import *
from places.models import *

# To do: django_filters.MethodFilter are commented because raising errors after version upgrade
# test and remove if not needed anymore

django_filters.filters.LOOKUP_TYPES = [
    ("", "---------"),
    ("exact", "Is equal to"),
    ("iexact", "Is equal to (case insensitive)"),
    ("not_exact", "Is not equal to"),
    ("lt", "Lesser than/before"),
    ("gt", "Greater than/after"),
    ("gte", "Greater than or equal to"),
    ("lte", "Lesser than or equal to"),
    ("startswith", "Starts with"),
    ("endswith", "Ends with"),
    ("contains", "Contains"),
    ("icontains", "Contains (case insensitive)"),
    ("not_contains", "Does not contain"),
]

YESNO = ((True, "Yes"), (False, "No"))

FULLYPARTLYEXCAVATED = (
    ("fully excavated", "fully excavated"),
    ("partly excavated", "partly excavated"),
)


class BurialSiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains", label="Burial Site name", help_text=False
    )
    alternative_name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Alternative name"
    )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(), help_text=False
    )
    topography = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="topography"),
        help_text=False,
    )
    distance_to_next_settlement = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains="distance"),
        help_text=False,
    )
    type_of_burial_site = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="type of burial site"
        ),
        help_text=False,
    )
    dating = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="dating"),
        help_text=False,
    )

    class Meta:
        model = BurialSite
        fields = "__all__"


class BurialGroupListFilter(django_filters.FilterSet):
    burial_group_id = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial group number"
    )
    burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site name"
    )
    burial_group_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial group type"
        ),
        help_text=False,
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Material"),
        help_text=False,
    )
    length = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    width = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    diameter = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    height = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )

    class Meta:
        model = BurialGroup
        fields = ["id", "burial_group_id", "burial_site__name"]


class BurialListFilter(django_filters.FilterSet):
    burial_id = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    burial_group = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial group"
    )
    burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site name"
    )
    C14_dendro = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        label="Absolute dating (C14/Dendro)",
        choices=YESNO,
    )
    absolute_age = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Absolute age"
    )
    burial_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Burial type"),
        help_text=False,
    )
    # i don't know what this is? there is no field 'individuals' in models
    # individuals = django_filters.ChoiceFilter(
    #     choices=YESNO, help_text=False,
    # )
    secondary_burial = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    displaced = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    extraordinary_burial = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    construction = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial construction"
        ),
        help_text=False,
    )
    arrangement = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial arrangement"
        ),
        help_text=False,
    )
    cover = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    cover_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Cover type"),
        help_text=False,
    )
    grave_pit_form = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Grave pit form"),
        help_text=False,
    )
    grave_pit_orientation = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Grave pit orientation"
        ),
        help_text=False,
    )
    length = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    width = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    diameter = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    height = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )

    class Meta:
        model = Burial
        fields = ["id", "burial_id", "burial_site__name"]


class UrnCoverListFilter(django_filters.FilterSet):
    cover_id = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Urn Inventory Number"
    )
    upside_down = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    fragment = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Basic shape of urn cover"
        ),
        help_text=False,
    )
    urn__burial__burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site"
    )
    urn__burial__burial_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Burial number"
    )

    class Meta:
        model = UrnCover
        fields = ["id", "cover_id"]


class UrnListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Burial number"
    )
    burial__burial_type__pref_label = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial type"
    )
    # burial__burial_type__pref_label = django_filters.ModelMultipleChoiceFilter(
    #     queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial type'),
    #     help_text=False,
    #     label="Burial type"
    # )
    basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Basic shape of urn"
        ),
        help_text=False,
    )
    urn_id = django_filters.CharFilter(
        lookup_expr="iexact", help_text=False, label="Urn Inventory Number"
    )
    urn_type = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Urn type"
    )
    variation = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Variation"
    )
    urncover_exists = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO, label="Urn cover exists"
    )

    class Meta:
        model = Urn
        fields = ["id", "urn_id"]


class GraveGoodListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Urn Inventory Number"
    )
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="GraveGoodObject"),
        help_text=False,
        label="Type",
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Material"),
        help_text=False,
    )
    condition = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Condition"),
        help_text=False,
    )
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
    )
    amount = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, label="amount_countable"
    )
    secondary_depostition = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        choices=YESNO,
        label="Secondary deposition",
    )

    class Meta:
        model = GraveGood
        fields = ["id", "name"]


class GraveGoodOtherListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Urn Inventory Number"
    )
    food = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    other_organic_grave_good = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
    )
    secondary_depostition = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        choices=YESNO,
        label="Secondary deposition",
    )

    class Meta:
        model = GraveGoodOther
        fields = [
            "id",
        ]


class DeadBodyRemainsListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Urn Inventory Number"
    )
    age = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Age"),
        help_text=False,
    )
    gender = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Gender"),
        help_text=False,
    )
    temperature = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Cremation temperature"
        ),
        help_text=False,
    )
    weight = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Weight"
    )
    pathology = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Pathology"
    )
    total_weight = django_filters.CharFilter(
        lookup_expr="iexact", help_text=False, label="Total weight"
    )
    amount_countable = django_filters.NumberFilter(lookup_expr="exact", help_text=False)
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Position of the cremated remains"
        ),
        help_text=False,
    )
    secondary_depostition = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        choices=YESNO,
        label="Secondary deposition",
    )

    class Meta:
        model = DeadBodyRemains
        fields = ["id", "age"]


class AnimalRemainsListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Urn Inventory Number"
    )
    species = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Species"),
        help_text=False,
    )
    age = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Age"
    )
    sex = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Sex"
    )
    weight = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Weight"
    )
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
    )
    amount_countable = django_filters.NumberFilter(lookup_expr="exact", help_text=False)
    secondary_depostition = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        choices=YESNO,
        label="Secondary deposition",
    )

    class Meta:
        model = AnimalRemains
        fields = ["id", "species"]


class MainListFilter(django_filters.FilterSet):
    burial_id = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    burial_group = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial group"
    )
    # BurialSite search fields
    burial_site__name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site name"
    )
    burial_site__alternative_name = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Burial site alternative name"
    )
    burial_site__location = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(), help_text=False
    )
    burial_site__topography = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Topography"),
        help_text=False,
    )
    burial_site__excavation = django_filters.ChoiceFilter(
        help_text=False, label="Excavation", choices=FULLYPARTLYEXCAVATED
    )
    burial_site__distance_to_next_settlement = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Distance to next settlement"
        ),
        help_text=False,
    )
    burial_site__type_of_burial_site = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Type of burial site"
        ),
        help_text=False,
        label="Type of burial site",
    )
    burial_site__disturbance = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False
    )
    burial_site__total_graves = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
        label=BurialSite._meta.get_field("total_graves").verbose_name,
    )
    burial_site__dating = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Dating"),
        help_text=False,
    )
    burial_site__absolute_dating = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False
    )
    # Burial search fields
    C14_dendro = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        label="Absolute dating (C14/Dendro)",
        choices=YESNO,
    )
    absolute_age = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Absolute age"
    )
    burial_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Burial type"),
        help_text=False,
    )
    # i don't know what this is? there is no field 'individuals' in models
    # individuals = django_filters.ChoiceFilter(
    #     choices=YESNO, help_text=False,
    # )
    secondary_burial = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    displaced = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    extraordinary_burial = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    construction = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial construction"
        ),
        help_text=False,
    )
    arrangement = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial arrangement"
        ),
        help_text=False,
    )
    cover = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    cover_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Cover type"),
        help_text=False,
    )
    grave_pit_form = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Grave pit form"),
        help_text=False,
    )
    grave_pit_orientation = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Grave pit orientation"
        ),
        help_text=False,
    )
    length = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    width = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    diameter = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    height = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
    )
    filling_objects = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial Filling Objects"
        ),
        help_text=False,
    )
    intentionally_deposited = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO
    )
    filling = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Burial Filling Type"
        ),
        help_text=False,
    )
    post_holes = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Post holes"
    )
    surface_identification_mark = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Surface Identification Mark"
    )
    erdgraebchen = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Erdgraebchen"
    )
    other_features = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Other features"
    )
    # Urn search fields
    urn__basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Basic shape of urn"
        ),
        help_text=False,
        label="Basic shape of urn",
    )
    urn__urn_type = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Urn type"
    )
    urn__variation = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Urn variation"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=False,
        label=Urn._meta.get_field("urn_id").verbose_name,
    )
    urn__urncover_exists = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO, label="Urn cover exists?"
    )
    # UrnCover search fields
    urn__urncover__basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Basic shape of urn cover"
        ),
        help_text=False,
        label="Basic shape of urn cover",
    )
    urn__urncover__upside_down = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        choices=YESNO,
        label="Urn cover upside down",
    )
    urn__urncover__fragment = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO, label="Fragment"
    )
    urn__urncover__cover_id = django_filters.CharFilter(
        lookup_expr="icontains",
        help_text=False,
        label=UrnCover._meta.get_field("cover_id").verbose_name,
    )
    # GraveGood search fields
    gravegood__name = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="GraveGoodObject"),
        help_text=False,
        label="Grave Good type",
    )
    gravegood__material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Material"),
        help_text=False,
        label="Grave Good material",
    )
    gravegood__condition = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Condition"),
        help_text=False,
        label="Grave Good condition",
    )
    gravegood__position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
        label="Grave Good position",
    )
    gravegood__amount_countable = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, distinct=True, label="Grave Good amount"
    )
    # GraveGoodOther search fields
    gravegoodother__food = django_filters.ChoiceFilter(
        null_label="Unknown", help_text=False, choices=YESNO, label="Food"
    )
    gravegoodother__other_organic_grave_good = django_filters.ChoiceFilter(
        null_label="Unknown",
        help_text=False,
        choices=YESNO,
        label="Other organic grave good",
    )
    gravegoodother__position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
        label="Organic Grave Good position",
    )
    gravegoodother__amount_countable = django_filters.NumberFilter(
        lookup_expr="exact",
        help_text=False,
        distinct=True,
        label="Organic Grave Good amount",
    )
    # DeadBodyRemains search fields
    deadbodyremains__age = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Age"),
        help_text=False,
        label="Anthropology age",
    )
    deadbodyremains__gender = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Gender"),
        help_text=False,
        label="Anthropology gender",
    )
    deadbodyremains__temperature = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            scheme__dc_title__iexact="Cremation temperature"
        ),
        help_text=False,
        label="Cremation temperature",
    )
    deadbodyremains__position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
        label="Anthropology position",
    )
    deadbodyremains__weight = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Anthropology weight in gram"
    )
    deadbodyremains__pathology = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Pathology"
    )
    deadbodyremains__total_weight = django_filters.CharFilter(
        lookup_expr="exact",
        help_text=False,
        label=DeadBodyRemains._meta.get_field("total_weight").verbose_name,
    )
    deadbodyremains__amount_countable = django_filters.NumberFilter(
        lookup_expr="exact", help_text=False, distinct=True, label="Anthropology amount"
    )
    # AnimalRemains search fields
    animalremains__species = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Species"),
        help_text=False,
        label="Species",
    )
    animalremains__age = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Animal remains age"
    )
    animalremains__sex = django_filters.CharFilter(
        lookup_expr="icontains", help_text=False, label="Animal remains sex"
    )
    animalremains__weight = django_filters.CharFilter(
        lookup_expr="exact", help_text=False, label="Animal remains weight"
    )
    animalremains__position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact="Position"),
        help_text=False,
        label="Animal remains position",
    )
    animalremains__amount_countable = django_filters.NumberFilter(
        lookup_expr="exact",
        help_text=False,
        distinct=True,
        label="Animal Remains amount",
    )

    class Meta:
        model = Burial
        fields = ["id", "burial_id", "burial_site__name"]
