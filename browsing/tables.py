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


class BurialGroupTable(tables.Table):
    # site_id = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')], accessor='id')
    burial_group_id = tables.LinkColumn('burials:burialgroup_detail', args=[A('pk')])
    # province_name = tables.Column(accessor='province.name', verbose_name='district')

    class Meta:
        model = BurialGroup
        fields = ['burial_group_id']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BurialTable(tables.Table):
    # site_id = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')], accessor='id')
    burial_id = tables.LinkColumn('burials:burial_detail', args=[A('pk')])
    # province_name = tables.Column(accessor='province.name', verbose_name='district')

    class Meta:
        model = Burial
        fields = ['burial_id']
        attrs = {"class": "table table-hover table-striped table-condensed"}
