from dal import autocomplete
from .models import SkosLabel, SkosConcept, SkosConceptScheme


class SkosLabelAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosLabel.objects.all()

        if self.q:
            qs = qs.filter(label__icontains=self.q)

        return qs


class SkosConceptAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = SkosConcept.objects.all()
        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class SkosConceptPrefLabalAC(autocomplete.Select2ListView):

    def get_list(self):
        concepts = SkosConcept.objects.filter(pref_label__icontains=self.q)
        pref_labels = set([x.pref_label for x in concepts])
        return pref_labels


class SkosConceptSchemeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConceptScheme.objects.all()

        if self.q:
            qs = qs.filter(dc_title__icontains=self.q)

        return qs
