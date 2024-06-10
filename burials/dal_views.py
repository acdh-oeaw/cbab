from dal import autocomplete
from vocabs.models import SkosConcept, SkosConceptScheme
from burials.models import *
from places.models import *
from django.db.models import Q


class PlaceAC(autocomplete.Select2QuerySetView):

    def qet_queryset(self):
        qs = Place.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class BookAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Book.objects.all()
        if self.q:
            qs = qs.filter(Q(author__icontains=self.q) | Q(title__icontains=self.q))

        return qs


class BurialSiteAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = BurialSite.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class BurialGroupAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = BurialGroup.objects.all()
        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs


class BurialAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Burial.objects.all()
        if self.q:
            qs = qs.filter(burial_id__icontains=self.q)

        return qs


class UrnCoverAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = UrnCover.objects.all()
        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs
