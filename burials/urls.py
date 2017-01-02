from django.conf.urls import url
from vocabs.models import SkosConcept
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
    # BurialGroup
    url(r'^burialgroup/(?P<pk>[0-9]+)$',
        views.BurialGroupDetailView.as_view(), name='burialgroup_detail'),
    url(r'^burialgroup/$', views.BurialGroupListView.as_view(),
        name='burialgroup_list'),
    url(r'^burialgroup/create/$', views.BurialGroupCreate.as_view(),
        name='burialgroup_create'),
    url(r'^burialgroup/update/(?P<pk>[0-9]+)$',
        views.BurialGroupUpdate.as_view(), name='burialgroup_update'),
    # Burial
    url(r'^burial/(?P<pk>[0-9]+)$',
        views.BurialDetailView.as_view(), name='burial_detail'),
    url(r'^burial/$', views.BurialListView.as_view(), name='burial_list'),
    url(r'^burial/create/$', views.BurialCreate.as_view(), name='burial_create'),
    url(r'^burial/update/(?P<pk>[0-9]+)$',
        views.BurialUpdate.as_view(), name='burial_update'),
    # UrnCover
    url(r'^urncover/(?P<pk>[0-9]+)$',
        views.UrnCoverDetailView.as_view(), name='urncover_detail'),
    url(r'^urncover/$', views.UrnCoverListView.as_view(), name='urncover_list'),
    url(r'^urncover/create/$', views.UrnCoverCreate.as_view(), name='urncover_create'),
    url(r'^urncover/update/(?P<pk>[0-9]+)$',
        views.UrnCoverUpdate.as_view(), name='urncover_update'),
    # Urn
    url(r'^urn/(?P<pk>[0-9]+)$',
        views.UrnDetailView.as_view(), name='urn_detail'),
    url(r'^urn/$', views.UrnListView.as_view(), name='urn_list'),
    url(r'^urn/create/$', views.UrnCreate.as_view(), name='urn_create'),
    url(r'^urn/update/(?P<pk>[0-9]+)$',
        views.UrnUpdate.as_view(), name='urn_update'),
    # GraveGood
    url(r'^gravegood/(?P<pk>[0-9]+)$',
        views.GraveGoodDetailView.as_view(), name='gravegood_detail'),
    url(r'^gravegood/$', views.GraveGoodListView.as_view(), name='gravegood_list'),
    url(r'^gravegood/create/$', views.GraveGoodCreate.as_view(),
        name='gravegood_create'),
    url(r'^gravegood/update/(?P<pk>[0-9]+)$',
        views.GraveGoodUpdate.as_view(), name='gravegood_update'),
    # GraveGoodOther
    url(r'^gravegoodother/(?P<pk>[0-9]+)$',
        views.GraveGoodOtherDetailView.as_view(), name='gravegoodother_detail'),
    url(r'^gravegoodother/$', views.GraveGoodOtherListView.as_view(),
        name='gravegoodother_list'),
    url(r'^gravegoodother/create/$', views.GraveGoodOtherCreate.as_view(),
        name='gravegoodother_create'),
    url(r'^gravegoodother/update/(?P<pk>[0-9]+)$',
        views.GraveGoodOtherUpdate.as_view(), name='gravegoodother_update'),
    # DeadBodyRemains
    url(r'^deadbodyremains/(?P<pk>[0-9]+)$',
        views.DeadBodyRemainsDetailView.as_view(), name='deadbodyremains_detail'),
    url(r'^deadbodyremains/$', views.DeadBodyRemainsListView.as_view(),
        name='deadbodyremains_list'),
    url(r'^deadbodyremains/create/$',
        views.DeadBodyRemainsCreate.as_view(), name='deadbodyremains_create'),
    url(r'^deadbodyremains/update/(?P<pk>[0-9]+)$',
        views.DeadBodyRemainsUpdate.as_view(), name='deadbodyremains_update'),
    url(
        r'^skos-constraint-ac/$', dal_views.SKOSConstraintAC.as_view(
            model=SkosConcept), name='skos-constraint-ac',
    ),
]
