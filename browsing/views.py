from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from burials.models import *
from .filters import *
from .forms import GenericFilterFormHelper
from .tables import *

# Create your views here.
class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class BurialSiteListView(GenericListView):
    model = BurialSite
    table_class = BurialSiteTable
    template_name = 'browsing/burialsite_list_generic.html'
    filter_class = BurialSiteListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        topography_names = []
        for x in SkosConcept.objects.all():
            topography_names.append(x.pref_label)
        context["topography_names"] = set(topography_names)
        return context


class BurialGroupListView(GenericListView):
    model = BurialGroup
    table_class = BurialGroupTable
    template_name = 'browsing/burialgroup_list_generic.html'
    filter_class = BurialGroupListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        topography_names = []
        for x in SkosConcept.objects.all():
            topography_names.append(x.pref_label)
        context["topography_names"] = set(topography_names)
        return context


class BurialListView(GenericListView):
    model = Burial
    table_class = BurialTable
    template_name = 'browsing/burial_list_generic.html'
    filter_class = BurialListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)
        return context


class UrnCoverListView(GenericListView):
    model = UrnCover
    table_class = UrnCoverTable
    template_name = 'browsing/urncover_list_generic.html'
    filter_class = UrnCoverListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context


class UrnListView(GenericListView):
    model = Urn
    table_class = UrnTable
    template_name = 'browsing/urn_list_generic.html'
    filter_class = UrnListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context

class GraveGoodListView(GenericListView):
    model = GraveGood
    table_class = GraveGoodTable
    template_name = 'browsing/gravegood_list_generic.html'
    filter_class = GraveGoodListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context


class GraveGoodOtherListView(GenericListView):
    model = GraveGoodOther
    table_class = GraveGoodOtherTable
    template_name = 'browsing/gravegoodother_list_generic.html'
    filter_class = GraveGoodOtherListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context


class DeadBodyRemainsListView(GenericListView):
    model = DeadBodyRemains
    table_class = DeadBodyRemainsTable
    template_name = 'browsing/deadbodyremains_list_generic.html'
    filter_class = DeadBodyRemainsListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context
