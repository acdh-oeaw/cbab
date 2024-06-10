from django.urls import re_path
from . import views

app_name = "vocabs"

urlpatterns = [
    re_path(r"^$", views.SkosConceptListView.as_view(), name="skosconcept_list"),
    re_path(
        r"^concepts/browse/$",
        views.SkosConceptFilterView.as_view(),
        name="browse_vocabs",
    ),
    re_path(
        r"^(?P<pk>[0-9]+)$",
        views.SkosConceptDetailView.as_view(),
        name="skosconcept_detail",
    ),
    re_path(r"^create/$", views.SkosConceptCreate.as_view(), name="skosconcept_create"),
    re_path(
        r"^update/(?P<pk>[0-9]+)$",
        views.SkosConceptUpdate.as_view(),
        name="skosconcept_update",
    ),
    re_path(
        r"^delete/(?P<pk>[0-9]+)$",
        views.SkosConceptDelete.as_view(),
        name="skosconcept_delete",
    ),
    re_path(
        r"^scheme/$",
        views.SkosConceptSchemeListView.as_view(),
        name="skosconceptscheme_list",
    ),
    re_path(
        r"^scheme/(?P<pk>[0-9]+)$",
        views.SkosConceptSchemeDetailView.as_view(),
        name="skosconceptscheme_detail",
    ),
    re_path(
        r"^scheme/create/$",
        views.SkosConceptSchemeCreate.as_view(),
        name="skosconceptscheme_create",
    ),
    re_path(
        r"^scheme/update/(?P<pk>[0-9]+)$",
        views.SkosConceptSchemeUpdate.as_view(),
        name="skosconceptscheme_update",
    ),
    re_path(r"^label/$", views.SkosLabelListView.as_view(), name="skoslabel_list"),
    re_path(
        r"^label/(?P<pk>[0-9]+)$",
        views.SkosLabelDetailView.as_view(),
        name="skoslabel_detail",
    ),
    re_path(
        r"^label/create/$", views.SkosLabelCreate.as_view(), name="skoslabel_create"
    ),
    re_path(
        r"^label/update/(?P<pk>[0-9]+)$",
        views.SkosLabelUpdate.as_view(),
        name="skoslabel_update",
    ),
]
