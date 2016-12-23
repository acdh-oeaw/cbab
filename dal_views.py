from dal import autocomplete
from vocabs.models import SkosConcept


class GenderAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConcept.objects.filter(scheme=24)

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs
