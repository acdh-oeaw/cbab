import django_filters
from . import forms
from browsing.forms import *
from burials.models import *
from vocabs.models import *
from places.models import *

# To do: django_filters.MethodFilter are commented because raising errors after version upgrade
# test and remove if not needed anymore

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]

YESNO = (
    (True, "Yes"),
    (False, "No")
)


class BurialSiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Burial Site name',
        help_text=False
    )
    alternative_name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Alternative name"
    )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(), help_text=False
    )
    topography = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='topography'),
        help_text=False
    )
    distance_to_next_settlement = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__icontains='distance'),
        help_text=False
    )
    type_of_burial_site = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='type of burial site'),
        help_text=False
    )
    dating = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='dating'),
        help_text=False
    )

    class Meta:
        model = BurialSite
        fields = '__all__'


class BurialGroupListFilter(django_filters.FilterSet):
    burial_group_id = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial group number"
    )
    burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site name"
    )
    burial_group_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial group type'),
        help_text=False
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Material'),
        help_text=False
    )
    length = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    width = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    diameter = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    height = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )

    class Meta:
        model = BurialGroup
        fields = ['id', 'burial_group_id', 'burial_site__name']


class BurialListFilter(django_filters.FilterSet):
    burial_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    burial_group = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial group"
    )
    burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site name"
    )
    C14_dendro = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        label="Absolute dating (C14/Dendro)",
        choices=YESNO
    )
    absolute_age = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Absolute age"
    )
    burial_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial type'),
        help_text=False
    )
    # i don't know what this is? there is no field 'individuals' in models
    # individuals = django_filters.ChoiceFilter(
    #     choices=YESNO, help_text=False,
    # )
    secondary_burial = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    displaced = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    extraordinary_burial = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    construction = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial construction'),
        help_text=False
    )
    arrangement = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial arrangement'),
        help_text=False
    )
    cover = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    cover_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Cover type'),
        help_text=False
    )
    grave_pit_form = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Grave pit form'),
        help_text=False
    )
    grave_pit_orientation = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Grave pit orientation'),
        help_text=False
    )
    length = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    width = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    diameter = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    height = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )

    class Meta:
        model = Burial
        fields = ['id', 'burial_id', 'burial_site__name']


class UrnCoverListFilter(django_filters.FilterSet):
    cover_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Urn Inventory Number"
    )
    upside_down = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    fragment = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Basic shape of urn cover'),
        help_text=False
    )
    urn__burial__burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site"
    )
    urn__burial__burial_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Burial number"
    )

    class Meta:
        model = UrnCover
        fields = ['id', 'cover_id']


class UrnListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Burial number"
    )
    burial__burial_type__pref_label = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial type"
    )
    # burial__burial_type__pref_label = django_filters.ModelMultipleChoiceFilter(
    #     queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial type'),
    #     help_text=False,
    #     label="Burial type"
    # )
    basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Basic shape of urn'),
        help_text=False
    )
    urn_id = django_filters.CharFilter(
        lookup_expr='iexact', help_text=False,
        label="Urn Inventory Number"
    )
    urn_type = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Urn type"
    )
    variation = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Variation"
    )
    urncover_exists = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO, label="Urn cover exists"
    )

    class Meta:
        model = Urn
        fields = ['id', 'urn_id']


class GraveGoodListFilter(django_filters.FilterSet):
    #burial_site_name = django_filters.MethodFilter(
    #    action='burialsite_name_custom_filter', help_text=False
    #    )
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Urn Inventory Number"
    )
    name = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='GraveGoodObject'),
        help_text=False, label="Type"
    )
    material = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Material'),
        help_text=False
    )
    condition = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Condition'),
        help_text=False
    )
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Position'),
        help_text=False
    )
    amount = django_filters.NumberFilter(
        lookup_expr='exact', help_text=False, name="amount_countable"
    )
    secondary_depostition = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO, label="Secondary deposition"
    )

    class Meta:
        model = GraveGood
        fields = ['id', 'name']


class GraveGoodOtherListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Urn Inventory Number"
    )
    food = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    other_organic_grave_good = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO
    )
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Position'),
        help_text=False
    )
    secondary_depostition = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO, label="Secondary deposition"
    )

    class Meta:
        model = GraveGoodOther
        fields = ['id', ]


class DeadBodyRemainsListFilter(django_filters.FilterSet):
    burial__burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Burial site"
    )
    burial__burial_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Burial number"
    )
    urn__urn_id = django_filters.CharFilter(
        lookup_expr='exact', help_text=False,
        label="Urn Inventory Number"
    )
    age = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Age'),
        help_text=False
    )
    gender = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Gender'),
        help_text=False
    )
    temperature = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Cremation temperature'),
        help_text=False
    )
    weight = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Weight"
    )
    pathology = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
        label="Pathology"
    )
    total_weight = django_filters.CharFilter(
        lookup_expr='iexact', help_text=False,
        label="Total weight"
    )
    amount_countable = django_filters.NumberFilter(
        lookup_expr='exact', help_text=False
    )
    position = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
        scheme__dc_title__iexact='Position of the cremated remains'),
        help_text=False
    )
    secondary_depostition = django_filters.ChoiceFilter(
        null_label='Unknown', help_text=False,
        choices=YESNO, label="Secondary deposition"
    )


    class Meta:
        model = DeadBodyRemains
        fields = ['id', 'age']


class AnimalRemainsListFilter(django_filters.FilterSet):
    #burial_site_name = django_filters.MethodFilter(
    #    action='burialsite_name_custom_filter', help_text=False
    #    )
    burial = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    species = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Species'),
        help_text=False
    )
    age = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    sex = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    weight = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    position = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    amount = django_filters.NumberFilter(
        lookup_expr='exact', help_text=False, name="amount_countable"
    )

    class Meta:
        model = AnimalRemains
        fields = ['id', 'species']

    def burialsite_name_custom_filter(self, queryset, value):
        return queryset.filter(burial__burial_site__name__icontains=value).distinct()
