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
        fields = ['name']

    # def topography_custom_filter(self, queryset, value):
    #     return queryset.filter(topography__pref_label__icontains=value).distinct()


class BurialGroupListFilter(django_filters.FilterSet):
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
        fields = ['burial_group_id', 'burial_site__name']


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
        fields = ['burial_id', 'burial_site__name']
