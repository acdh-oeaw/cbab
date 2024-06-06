from django_tables2 import SingleTableView, RequestConfig
from burials.models import *
from .filters import *
from .forms import GenericFilterFormHelper
from .tables import *
import csv
import time
import datetime
from django.http import HttpResponse


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = "filter"
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(
            self.request, paginate={"page": 1, "per_page": self.paginate_by}
        ).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class BurialSiteListView(GenericListView):
    model = BurialSite
    table_class = BurialSiteTable
    template_name = "browsing/burialsite_list_generic.html"
    filter_class = BurialSiteListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        alternative_names = []
        for x in BurialSite.objects.all():
            alternative_names.append(x.alternative_name)
        context["alternative_names"] = set(alternative_names)

        return context


class BurialGroupListView(GenericListView):
    model = BurialGroup
    table_class = BurialGroupTable
    template_name = "browsing/burialgroup_list_generic.html"
    filter_class = BurialGroupListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        burialgroup_ids = []
        for x in BurialGroup.objects.all():
            burialgroup_ids.append(x.burial_group_id)
        context["burialgroup_ids"] = set(burialgroup_ids)

        return context


class BurialListView(GenericListView):
    model = Burial
    table_class = BurialTable
    template_name = "browsing/burial_list_generic.html"
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
    template_name = "browsing/urncover_list_generic.html"
    filter_class = UrnCoverListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context


class UrnListView(GenericListView):
    model = Urn
    table_class = UrnTable
    template_name = "browsing/urn_list_generic.html"
    filter_class = UrnListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        return context


class GraveGoodListView(GenericListView):
    model = GraveGood
    table_class = GraveGoodTable
    template_name = "browsing/gravegood_list_generic.html"
    filter_class = GraveGoodListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        gravegood_names = []
        for x in SkosConcept.objects.filter(scheme__dc_title__iexact="Grave good name"):
            gravegood_names.append(x.pref_label)
        context["gravegood_names"] = set(gravegood_names)

        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        return context


class GraveGoodOtherListView(GenericListView):
    model = GraveGoodOther
    table_class = GraveGoodOtherTable
    template_name = "browsing/gravegoodother_list_generic.html"
    filter_class = GraveGoodOtherListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        return context


class DeadBodyRemainsListView(GenericListView):
    model = DeadBodyRemains
    table_class = DeadBodyRemainsTable
    template_name = "browsing/deadbodyremains_list_generic.html"
    filter_class = DeadBodyRemainsListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        return context


class AnimalRemainsListView(GenericListView):
    model = AnimalRemains
    table_class = AnimalRemainsTable
    template_name = "browsing/animalremains_list_generic.html"
    filter_class = AnimalRemainsListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        burialsite_names = []
        for x in BurialSite.objects.all():
            burialsite_names.append(x.name)
        context["burialsite_names"] = set(burialsite_names)

        return context


class MainListView(GenericListView):
    model = Burial
    table_class = BurialTable
    template_name = "browsing/main_list_generic.html"
    filter_class = MainListFilter
    formhelper_class = MainListFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        burialsites = []
        for x in self.get_queryset():
            burialsites.append(x.burial_site)
        context["burialsites"] = set(burialsites)

        burials = []
        for x in self.get_queryset():
            burials.append(x)
        context["burials"] = set(burials)
        return context


class MainListDownloadView(GenericListView):
    model = Burial
    table_class = BurialTable
    template_name = "browsing/main_list_generic.html"
    filter_class = MainListFilter
    formhelper_class = MainListFilterFormHelper

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime(
            "%Y-%m-%d-%H-%M-%S"
        )
        response = HttpResponse(content_type="text/csv")
        filename = "cbab_export_{}".format(timestamp)
        response["Content-Disposition"] = 'attachment; filename="{}.csv"'.format(
            filename
        )
        writer = csv.writer(response, delimiter=",")
        writer.writerow(
            [
                "Burial ID",
                "Burial number",
                "Burial site",
                "Place name",
                "Province",
                "Geonames ID",
                "Latitude",
                "Longitude",
                "Burial group",
                "Burial type",
                "Absolute dating (C14/Dendro)",
                "Absolute age",
                "Secondary burial",
                "Secondary burial text",
                "Displaced",
                "Displaced text",
                "Extraordinary burial",
                "Extraordinary burial text",
                "Inhumation burial type",
                "Bi-ritual burial type",
                "Construction",
                "Arrangement",
                "Cover",
                "Cover type",
                "Grave pit form",
                "Grave pit orientation",
                "Length",
                "Width",
                "Diameter",
                "Heigth",
                "Filling objects",
                "Interntionally deposited",
                "Filling",
                "Post holes",
                "Surface identification mark",
                "Erdgraebchen",
                "Other features",
                "Urn",
                "Grave good",
                "Grave good amount",
                "Anthropology",
                "Anthropology amount",
                "Organic grave good",
                "Animal remains",
                "Animal remains amount",
            ]
        )
        for obj in self.get_queryset():
            writer.writerow(
                [
                    obj.id,
                    obj.burial_id,
                    obj.burial_site.name,
                    obj.burial_site.location.name,
                    obj.burial_site.location.province,
                    obj.burial_site.location.geonames_id,
                    obj.burial_site.lat,
                    obj.burial_site.lng,
                    obj.burial_group,
                    obj.burial_type,
                    obj.get_C14_dendro_display(),
                    obj.absolute_age,
                    obj.get_secondary_burial_display(),
                    obj.secondary_burial_text,
                    obj.get_displaced_display(),
                    obj.displaced_text,
                    obj.get_extraordinary_burial_display(),
                    obj.extraordinary_burial_text,
                    obj.inhumation_burial_type,
                    obj.bi_ritual_burial_type,
                    obj.construction,
                    obj.arrangement,
                    obj.get_cover_display(),
                    obj.cover_type,
                    obj.grave_pit_form,
                    obj.grave_pit_orientation,
                    obj.length,
                    obj.width,
                    obj.diameter,
                    obj.height,
                    "; ".join([obj.pref_label for obj in obj.filling_objects.all()]),
                    obj.get_intentionally_deposited_display(),
                    obj.filling,
                    obj.post_holes,
                    obj.surface_identification_mark,
                    obj.erdgraebchen,
                    obj.other_features,
                    "; ".join([str(x) for x in obj.urn_set.all()]),
                    "; ".join([str(x.name) for x in obj.gravegood_set.all()]),
                    obj.amount_related_gravegoods,
                    "; ".join([str(x) for x in obj.deadbodyremains_set.all()]),
                    obj.amount_related_deadbodyremains,
                    "; ".join([str(x) for x in obj.gravegoodother_set.all()]),
                    "; ".join([str(x.species) for x in obj.animalremains_set.all()]),
                    obj.amount_related_organic,
                ]
            )
        return response
