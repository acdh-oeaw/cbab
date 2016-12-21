import django_filters
from .models import SkosConcept


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


class SkosConceptFilter(django_filters.FilterSet):
    pref_label = django_filters.CharFilter(lookup_expr='icontains')
    scheme = django_filters.MethodFilter(action='custom_filter_scheme')

    class Meta:
        model = SkosConcept
        fields = ['pref_label', 'scheme']

    def custom_filter_scheme(self, queryset, value):
        return queryset.filter(scheme__legacy_id__icontains=value).distinct()
