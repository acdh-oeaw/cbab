from django.urls import re_path
from . import dal_views
from .models import SkosLabel, SkosConcept, SkosConceptScheme

app_name = "vocabs"

urlpatterns = [
    re_path(
        r"^skoslabel-autocomplete/$",
        dal_views.SkosLabelAC.as_view(
            model=SkosLabel,
            create_field="label",
        ),
        name="skoslabel-autocomplete",
    ),
    re_path(
        r"^skosconceptscheme-autocomplete/$",
        dal_views.SkosConceptSchemeAC.as_view(
            model=SkosConceptScheme,
            create_field="dc_title",
        ),
        name="skosconceptscheme-autocomplete",
    ),
    re_path(
        r"^skosconcept-autocomplete/$",
        dal_views.SkosConceptAC.as_view(
            model=SkosConcept,
            create_field="pref_label",
        ),
        name="skosconcept-autocomplete",
    ),
    re_path(
        r"^skosconcept-pref-label-autocomplete/$",
        dal_views.SkosConceptPrefLabalAC.as_view(),
        name="skosconcept-label-ac",
    ),
    re_path(
        r"^skos-constraint-ac/$",
        dal_views.SKOSConstraintAC.as_view(model=SkosConcept),
        name="skos-constraint-ac",
    ),
    re_path(
        r"^skos-constraint-no-hierarchy-ac/$",
        dal_views.SKOSConstraintACNoHierarchy.as_view(model=SkosConcept),
        name="skos-constraint-no-hierarchy-ac",
    ),
]
