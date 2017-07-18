import django_filters
from . import forms
from browsing.forms import *
from burials.models import *
from vocabs.models import *
from places.models import *

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
    ('', '---------'),
    ("yes", "yes"),
    ("no", "no")
)


class BurialSiteListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Burial Site name',
        help_text=False
    )
    alternative_name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False
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


class BurialGroupListFilter(django_filters.FilterSet):
    burial_group_id = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False
    )
    burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False
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
        lookup_expr='icontains', help_text=False
    )
    burial_site__name = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False
    )
    C14_dendro = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    absolute_age = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    burial_type = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Burial type'),
        help_text=False
    )
    individuals = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )
    secondary_burial = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )
    displaced = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )
    extraordinary_burial = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
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
        choices=YESNO, help_text=False,
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
    upside_down = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )
    fragment = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )
    basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Basic shape of urn cover'),
        help_text=False
    )

    class Meta:
        model = UrnCover
        fields = ['id', 'cover_id']


class UrnListFilter(django_filters.FilterSet):
    burial_site_name = django_filters.MethodFilter(
        action='burialsite_name_custom_filter', help_text=False
        )
    burial = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    basic_shape = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Basic shape of urn'),
        help_text=False
    )
    urn_id = django_filters.CharFilter(
        lookup_expr='iexact', help_text=False,
    )
    urn_type = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    variation = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    cover = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )

    class Meta:
        model = Urn
        fields = ['id', 'urn_id']

    def burialsite_name_custom_filter(self, queryset, value):
        return queryset.filter(burial__burial_site__name__icontains=value).distinct()


class GraveGoodListFilter(django_filters.FilterSet):
    burial_site_name = django_filters.MethodFilter(
        action='burialsite_name_custom_filter', help_text=False
        )
    burial = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    name = django_filters.MethodFilter(
        action='gravegood_name_custom_filter', help_text=False
        )
    # name = django_filters.ModelMultipleChoiceFilter(
    #     queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='Grave good name'),
    #     help_text=False,
    # )
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

    class Meta:
        model = GraveGood
        fields = ['id', 'name']

    def gravegood_name_custom_filter(self, queryset, value):
        return queryset.filter(name__pref_label__icontains=value).distinct()

    def burialsite_name_custom_filter(self, queryset, value):
        return queryset.filter(burial__burial_site__name__icontains=value).distinct()


class GraveGoodOtherListFilter(django_filters.FilterSet):
    burial_site_name = django_filters.MethodFilter(
        action='burialsite_name_custom_filter', help_text=False
        )
    burial = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    food = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )
    other_organic_grave_good = django_filters.ChoiceFilter(
        choices=YESNO, help_text=False,
    )

    class Meta:
        model = GraveGoodOther
        fields = ['id', 'burial']

    def burialsite_name_custom_filter(self, queryset, value):
        return queryset.filter(burial__burial_site__name__icontains=value).distinct()


class DeadBodyRemainsListFilter(django_filters.FilterSet):
    burial_site_name = django_filters.MethodFilter(
        action='burialsite_name_custom_filter', help_text=False
        )
    burial = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
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
    )
    pathology = django_filters.CharFilter(
        lookup_expr='icontains', help_text=False,
    )
    total_weight = django_filters.CharFilter(
        lookup_expr='iexact', help_text=False,
    )


    class Meta:
        model = DeadBodyRemains
        fields = ['id', 'age']

    def burialsite_name_custom_filter(self, queryset, value):
        return queryset.filter(burial__burial_site__name__icontains=value).distinct()


class AnimalRemainsListFilter(django_filters.FilterSet):
    burial_site_name = django_filters.MethodFilter(
        action='burialsite_name_custom_filter', help_text=False
        )
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
