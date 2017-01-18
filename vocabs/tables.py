import django_tables2 as tables
from django_tables2.utils import A
from vocabs.models import *


class SkosConceptTable(tables.Table):
    pref_label = tables.LinkColumn('vocabs:skosconcept_detail', args=[A('pk')])
    # all_schemes = tables.Column(verbose_name='in SkosScheme', orderable=False)

    class Meta:
        model = SkosConcept
        fields = ['pref_label', 'namespace']
        attrs = {"class": "table table-hover table-striped table-condensed"}
