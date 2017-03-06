from django.conf.urls import url
from vocabs.models import SkosConcept
from burials.models import *
from bib.models import *
from . import views, dal_views


urlpatterns = [
    # BurialSite
    url(r'^burialsite/(?P<pk>[0-9]+)$',
        views.BurialSiteDetailView.as_view(), name='burialsite_detail'),
    url(r'^burialsite/$', views.BurialSiteListView.as_view(), name='burialsite_list'),
    url(r'^burialsite/create/$', views.BurialSiteCreate.as_view(),
        name='burialsite_create'),
    url(r'^burialsite/update/(?P<pk>[0-9]+)$',
        views.BurialSiteUpdate.as_view(), name='burialsite_update'),
    url(r'^burialsite/delete/(?P<pk>[0-9]+)$',
        views.BurialSiteDelete.as_view(), name='burialsite_delete'),
    # BurialGroup
    url(r'^burialgroup/(?P<pk>[0-9]+)$',
        views.BurialGroupDetailView.as_view(), name='burialgroup_detail'),
    url(r'^burialgroup/$', views.BurialGroupListView.as_view(),
        name='burialgroup_list'),
    url(r'^burialgroup/create/$', views.BurialGroupCreate.as_view(),
        name='burialgroup_create'),
    url(r'^burialgroup/update/(?P<pk>[0-9]+)$',
        views.BurialGroupUpdate.as_view(), name='burialgroup_update'),
    url(r'^burialgroup/delete/(?P<pk>[0-9]+)$',
        views.BurialGroupDelete.as_view(), name='burialgroup_delete'),
    # Burial
    url(r'^burial/(?P<pk>[0-9]+)$',
        views.BurialDetailView.as_view(), name='burial_detail'),
    url(r'^burial/$', views.BurialListView.as_view(), name='burial_list'),
    url(r'^burial/create/$', views.BurialCreate.as_view(), name='burial_create'),
    url(r'^burial/update/(?P<pk>[0-9]+)$',
        views.BurialUpdate.as_view(), name='burial_update'),
    url(r'^burial/delete/(?P<pk>[0-9]+)$',
        views.BurialDelete.as_view(), name='burial_delete'),
    # Burialfilling
    url(r'^fillingobject/(?P<pk>[0-9]+)$',
        views.FillingObjectDetailView.as_view(), name='burialfilling_detail'),
    url(r'^fillingobject/$', views.FillingObjectListView.as_view(), name='burialfilling_list'),
    url(r'^fillingobject/create/$', views.FillingObjectCreate.as_view(),
        name='burialfilling_create'),
    url(r'^fillingobject/update/(?P<pk>[0-9]+)$',
        views.FillingObjectUpdate.as_view(), name='burialfilling_update'),
    url(r'^fillingobject/delete/(?P<pk>[0-9]+)$',
        views.FillingObjectDelete.as_view(), name='burialfilling_delete'),
    # UrnCover
    url(r'^urncover/(?P<pk>[0-9]+)$',
        views.UrnCoverDetailView.as_view(), name='urncover_detail'),
    url(r'^urncover/$', views.UrnCoverListView.as_view(), name='urncover_list'),
    url(r'^urncover/create/$', views.UrnCoverCreate.as_view(), name='urncover_create'),
    url(r'^urncover/update/(?P<pk>[0-9]+)$',
        views.UrnCoverUpdate.as_view(), name='urncover_update'),
    url(r'^urncover/delete/(?P<pk>[0-9]+)$',
        views.UrnCoverDelete.as_view(), name='urncover_delete'),
    # Urn
    url(r'^urn/(?P<pk>[0-9]+)$',
        views.UrnDetailView.as_view(), name='urn_detail'),
    url(r'^urn/$', views.UrnListView.as_view(), name='urn_list'),
    url(r'^urn/create/$', views.UrnCreate.as_view(), name='urn_create'),
    url(r'^urn/update/(?P<pk>[0-9]+)$',
        views.UrnUpdate.as_view(), name='urn_update'),
    url(r'^urn/delete/(?P<pk>[0-9]+)$',
        views.UrnDelete.as_view(), name='urn_delete'),
    # GraveGood
    url(r'^gravegood/(?P<pk>[0-9]+)$',
        views.GraveGoodDetailView.as_view(), name='gravegood_detail'),
    url(r'^gravegood/$', views.GraveGoodListView.as_view(), name='gravegood_list'),
    url(r'^gravegood/create/$', views.GraveGoodCreate.as_view(),
        name='gravegood_create'),
    url(r'^gravegood/update/(?P<pk>[0-9]+)$',
        views.GraveGoodUpdate.as_view(), name='gravegood_update'),
    url(r'^gravegood/delete/(?P<pk>[0-9]+)$',
        views.GraveGoodDelete.as_view(), name='gravegood_delete'),
    # GraveGoodOther
    url(r'^gravegoodother/(?P<pk>[0-9]+)$',
        views.GraveGoodOtherDetailView.as_view(), name='gravegoodother_detail'),
    url(r'^gravegoodother/$', views.GraveGoodOtherListView.as_view(),
        name='gravegoodother_list'),
    url(r'^gravegoodother/create/$', views.GraveGoodOtherCreate.as_view(),
        name='gravegoodother_create'),
    url(r'^gravegoodother/update/(?P<pk>[0-9]+)$',
        views.GraveGoodOtherUpdate.as_view(), name='gravegoodother_update'),
    url(r'^gravegoodother/delete/(?P<pk>[0-9]+)$',
        views.GraveGoodOtherDelete.as_view(), name='gravegoodother_delete'),
    # DeadBodyRemains
    url(r'^deadbodyremains/(?P<pk>[0-9]+)$',
        views.DeadBodyRemainsDetailView.as_view(), name='deadbodyremains_detail'),
    url(r'^deadbodyremains/$', views.DeadBodyRemainsListView.as_view(),
        name='deadbodyremains_list'),
    url(r'^deadbodyremains/create/$',
        views.DeadBodyRemainsCreate.as_view(), name='deadbodyremains_create'),
    url(r'^deadbodyremains/update/(?P<pk>[0-9]+)$',
        views.DeadBodyRemainsUpdate.as_view(), name='deadbodyremains_update'),
    url(r'^deadbodyremains/delete/(?P<pk>[0-9]+)$',
        views.DeadBodyRemainsDelete.as_view(), name='deadbodyremains_delete'),
    # AnimalRemains
    url(r'^animalremains/(?P<pk>[0-9]+)$',
        views.AnimalRemainsDetailView.as_view(), name='animalremains_detail'),
    url(r'^animalremains/$', views.AnimalRemainsListView.as_view(),
        name='animalremains_list'),
    url(r'^animalremains/create/$',
        views.AnimalRemainsCreate.as_view(), name='animalremains_create'),
    url(r'^animalremains/update/(?P<pk>[0-9]+)$',
        views.AnimalRemainsUpdate.as_view(), name='animalremains_update'),
    url(r'^animalremains/delete/(?P<pk>[0-9]+)$',
        views.AnimalRemainsDelete.as_view(), name='animalremains_delete'),
    #Autocomplete fields
    url(
        r'^skos-constraint-ac/$', dal_views.SKOSConstraintAC.as_view(
            model=SkosConcept), name='skos-constraint-ac',
    ),
    url(
        r'^place-autocomplete/$', dal_views.PlaceAC.as_view(
            model=Place), name='place-autocomplete',
    ),
    url(
        r'^book-autocomplete/$', dal_views.BookAC.as_view(
            model=Book), name='book-autocomplete',
    ),
    url(
        r'^burialsite-autocomplete/$', dal_views.BurialSiteAC.as_view(
            model=BurialSite), name='burialsite-autocomplete',
    ),
    url(
        r'^burialgroup-autocomplete/$', dal_views.BurialGroupAC.as_view(
            model=BurialGroup), name='burialgroup-autocomplete',
    ),
    url(
        r'^burial-autocomplete/$', dal_views.BurialAC.as_view(
            model=Burial), name='burial-autocomplete',
    ),
    url(
        r'^urncover-autocomplete/$', dal_views.UrnCoverAC.as_view(
            model=UrnCover), name='urncover-autocomplete',
    ),

]
