from dal import autocomplete
from vocabs.models import SkosConcept, SkosConceptScheme


class GenderAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):

        scheme = self.kwargs['scheme']
        try:
            selected_scheme = SkosConceptScheme.objects.get(id=scheme)
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.filter(scheme=24)

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs
