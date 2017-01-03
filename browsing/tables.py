import django_tables2 as tables
from django_tables2.utils import A
from burials.models import *


class BurialSiteTable(tables.Table):
    # site_id = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')], accessor='id')
    name = tables.LinkColumn('burials:burialsite_detail', args=[A('pk')])
    # province_name = tables.Column(accessor='province.name', verbose_name='district')

    class Meta:
        model = BurialSite
        fields = ['name']
        attrs = {"class": "table table-hover table-striped table-condensed"}
