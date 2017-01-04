import django_tables2 as tables
from django_tables2.utils import A
from burials.models import *


class BurialSiteTable(tables.Table):
    db_id = tables.LinkColumn('burials:burialsite_detail', args=[A('pk')], accessor='id')
    name = tables.LinkColumn('burials:burialsite_detail', args=[A('pk')])

    class Meta:
        model = BurialSite
        fields = ['db_id', 'name', 'type_of_burial_site']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BurialGroupTable(tables.Table):
    # site_id = tables.LinkColumn('publicrecords:site_detail', args=[A('pk')], accessor='id', verbose_name='district')
    db_id = tables.LinkColumn('burials:burialgroup_detail', args=[A('pk')], accessor='id')
    burial_group_id = tables.LinkColumn('burials:burialgroup_detail', args=[A('pk')])
    burial_site = tables.Column()

    class Meta:
        model = BurialGroup
        fields = ['db_id', 'burial_group_id', 'burial_group_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BurialTable(tables.Table):
    db_id = tables.LinkColumn('burials:burial_detail', args=[A('pk')], accessor='id')
    burial_id = tables.LinkColumn('burials:burial_detail', args=[A('pk')])

    class Meta:
        model = Burial
        fields = ['db_id', 'burial_id', 'burial_site']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class UrnCoverTable(tables.Table):
    db_id = tables.LinkColumn('burials:urncover_detail', args=[A('pk')], accessor='id')
    cover_id = tables.LinkColumn('burials:urncover_detail', args=[A('pk')])

    class Meta:
        model = UrnCover
        fields = ['db_id', 'cover_id', 'basic_shape']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class UrnTable(tables.Table):
    db_id = tables.LinkColumn('burials:urn_detail', args=[A('pk')], accessor='id')
    urn_id = tables.LinkColumn('burials:urn_detail', args=[A('pk')])
    burial_site = tables.Column(accessor='burial.burial_site.name', verbose_name='burial site name')

    class Meta:
        model = Urn
        fields = ['db_id','urn_id', 'basic_shape']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class GraveGoodTable(tables.Table):
    db_id = tables.LinkColumn('burials:gravegood_detail', args=[A('pk')], accessor='id')
    name = tables.LinkColumn('burials:gravegood_detail', args=[A('pk')])
    burial_site = tables.Column(accessor='burial.burial_site.name', verbose_name='burial site name')

    class Meta:
        model = GraveGood
        fields = ['db_id','name', 'material']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class GraveGoodOtherTable(tables.Table):
    db_id = tables.LinkColumn('burials:gravegoodother_detail', args=[A('pk')], accessor='id')
    burial_site = tables.Column(accessor='burial.burial_site.name', verbose_name='burial site name')

    class Meta:
        model = GraveGood
        fields = ['db_id','burial']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class DeadBodyRemainsTable(tables.Table):
    db_id = tables.LinkColumn('burials:deadbodyremains_detail', args=[A('pk')], accessor='id')
    burial_site = tables.Column(accessor='burial.burial_site.name', verbose_name='burial site name')

    class Meta:
        model = GraveGood
        fields = ['db_id','age']
        attrs = {"class": "table table-hover table-striped table-condensed"}
