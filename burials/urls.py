from django.urls import re_path
from . import views, dal_views

app_name = "burials"

urlpatterns = [
    # BurialSite
    re_path(
        r"^burialsite/(?P<pk>[0-9]+)$",
        views.BurialSiteDetailView.as_view(),
        name="burialsite_detail",
    ),
    re_path(r"^burialsite/$", views.BurialSiteListView.as_view(), name="burialsite_list"),
    re_path(
        r"^burialsite/create/$",
        views.BurialSiteCreate.as_view(),
        name="burialsite_create",
    ),
    re_path(
        r"^burialsite/update/(?P<pk>[0-9]+)$",
        views.BurialSiteUpdate.as_view(),
        name="burialsite_update",
    ),
    re_path(
        r"^burialsite/delete/(?P<pk>[0-9]+)$",
        views.BurialSiteDelete.as_view(),
        name="burialsite_delete",
    ),
    # BurialGroup
    re_path(
        r"^burialgroup/(?P<pk>[0-9]+)$",
        views.BurialGroupDetailView.as_view(),
        name="burialgroup_detail",
    ),
    re_path(
        r"^burialgroup/$", views.BurialGroupListView.as_view(), name="burialgroup_list"
    ),
    re_path(
        r"^burialgroup/create/$",
        views.BurialGroupCreate.as_view(),
        name="burialgroup_create",
    ),
    re_path(
        r"^burialgroup/update/(?P<pk>[0-9]+)$",
        views.BurialGroupUpdate.as_view(),
        name="burialgroup_update",
    ),
    re_path(
        r"^burialgroup/delete/(?P<pk>[0-9]+)$",
        views.BurialGroupDelete.as_view(),
        name="burialgroup_delete",
    ),
    # Burial
    re_path(
        r"^burial/(?P<pk>[0-9]+)$",
        views.BurialDetailView.as_view(),
        name="burial_detail",
    ),
    re_path(r"^burial/$", views.BurialListView.as_view(), name="burial_list"),
    re_path(r"^burial/create/$", views.BurialCreate.as_view(), name="burial_create"),
    re_path(
        r"^burial/update/(?P<pk>[0-9]+)$",
        views.BurialUpdate.as_view(),
        name="burial_update",
    ),
    re_path(
        r"^burial/delete/(?P<pk>[0-9]+)$",
        views.BurialDelete.as_view(),
        name="burial_delete",
    ),
    # UrnCover
    re_path(
        r"^urncover/(?P<pk>[0-9]+)$",
        views.UrnCoverDetailView.as_view(),
        name="urncover_detail",
    ),
    re_path(r"^urncover/$", views.UrnCoverListView.as_view(), name="urncover_list"),
    re_path(r"^urncover/create/$", views.UrnCoverCreate.as_view(), name="urncover_create"),
    re_path(
        r"^urncover/update/(?P<pk>[0-9]+)$",
        views.UrnCoverUpdate.as_view(),
        name="urncover_update",
    ),
    re_path(
        r"^urncover/delete/(?P<pk>[0-9]+)$",
        views.UrnCoverDelete.as_view(),
        name="urncover_delete",
    ),
    # Urn
    re_path(r"^urn/(?P<pk>[0-9]+)$", views.UrnDetailView.as_view(), name="urn_detail"),
    re_path(r"^urn/$", views.UrnListView.as_view(), name="urn_list"),
    re_path(r"^urn/create/$", views.UrnCreate.as_view(), name="urn_create"),
    re_path(r"^urn/update/(?P<pk>[0-9]+)$", views.UrnUpdate.as_view(), name="urn_update"),
    re_path(r"^urn/delete/(?P<pk>[0-9]+)$", views.UrnDelete.as_view(), name="urn_delete"),
    # GraveGood
    re_path(
        r"^gravegood/(?P<pk>[0-9]+)$",
        views.GraveGoodDetailView.as_view(),
        name="gravegood_detail",
    ),
    re_path(r"^gravegood/$", views.GraveGoodListView.as_view(), name="gravegood_list"),
    re_path(
        r"^gravegood/create/$", views.GraveGoodCreate.as_view(), name="gravegood_create"
    ),
    re_path(
        r"^gravegood/update/(?P<pk>[0-9]+)$",
        views.GraveGoodUpdate.as_view(),
        name="gravegood_update",
    ),
    re_path(
        r"^gravegood/delete/(?P<pk>[0-9]+)$",
        views.GraveGoodDelete.as_view(),
        name="gravegood_delete",
    ),
    # GraveGoodOther
    re_path(
        r"^gravegoodother/(?P<pk>[0-9]+)$",
        views.GraveGoodOtherDetailView.as_view(),
        name="gravegoodother_detail",
    ),
    re_path(
        r"^gravegoodother/$",
        views.GraveGoodOtherListView.as_view(),
        name="gravegoodother_list",
    ),
    re_path(
        r"^gravegoodother/create/$",
        views.GraveGoodOtherCreate.as_view(),
        name="gravegoodother_create",
    ),
    re_path(
        r"^gravegoodother/update/(?P<pk>[0-9]+)$",
        views.GraveGoodOtherUpdate.as_view(),
        name="gravegoodother_update",
    ),
    re_path(
        r"^gravegoodother/delete/(?P<pk>[0-9]+)$",
        views.GraveGoodOtherDelete.as_view(),
        name="gravegoodother_delete",
    ),
    # DeadBodyRemains
    re_path(
        r"^deadbodyremains/(?P<pk>[0-9]+)$",
        views.DeadBodyRemainsDetailView.as_view(),
        name="deadbodyremains_detail",
    ),
    re_path(
        r"^deadbodyremains/$",
        views.DeadBodyRemainsListView.as_view(),
        name="deadbodyremains_list",
    ),
    re_path(
        r"^deadbodyremains/create/$",
        views.DeadBodyRemainsCreate.as_view(),
        name="deadbodyremains_create",
    ),
    re_path(
        r"^deadbodyremains/update/(?P<pk>[0-9]+)$",
        views.DeadBodyRemainsUpdate.as_view(),
        name="deadbodyremains_update",
    ),
    re_path(
        r"^deadbodyremains/delete/(?P<pk>[0-9]+)$",
        views.DeadBodyRemainsDelete.as_view(),
        name="deadbodyremains_delete",
    ),
    # AnimalRemains
    re_path(
        r"^animalremains/(?P<pk>[0-9]+)$",
        views.AnimalRemainsDetailView.as_view(),
        name="animalremains_detail",
    ),
    re_path(
        r"^animalremains/$",
        views.AnimalRemainsListView.as_view(),
        name="animalremains_list",
    ),
    re_path(
        r"^animalremains/create/$",
        views.AnimalRemainsCreate.as_view(),
        name="animalremains_create",
    ),
    re_path(
        r"^animalremains/update/(?P<pk>[0-9]+)$",
        views.AnimalRemainsUpdate.as_view(),
        name="animalremains_update",
    ),
    re_path(
        r"^animalremains/delete/(?P<pk>[0-9]+)$",
        views.AnimalRemainsDelete.as_view(),
        name="animalremains_delete",
    ),
    # Autocomplete fields
    re_path(
        r"^place-autocomplete/$",
        dal_views.PlaceAC.as_view(),
        name="place-autocomplete",
    ),
    re_path(
        r"^book-autocomplete/$",
        dal_views.BookAC.as_view(),
        name="book-autocomplete",
    ),
    re_path(
        r"^burialsite-autocomplete/$",
        dal_views.BurialSiteAC.as_view(),
        name="burialsite-autocomplete",
    ),
    re_path(
        r"^burialgroup-autocomplete/$",
        dal_views.BurialGroupAC.as_view(),
        name="burialgroup-autocomplete",
    ),
    re_path(
        r"^burial-autocomplete/$",
        dal_views.BurialAC.as_view(),
        name="burial-autocomplete",
    ),
    re_path(
        r"^urncover-autocomplete/$",
        dal_views.UrnCoverAC.as_view(),
        name="urncover-autocomplete",
    ),
]
