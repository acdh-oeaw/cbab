from django.urls import include, re_path
from django.contrib import admin
from rest_framework import routers
from places.apis_views import PlaceViewSet
from bib.api_views import BookViewSet
from burials import api_views as burial_api_views
from vocabs import api_views

router = routers.DefaultRouter()
router.register(r"burialsites", burial_api_views.BurialSiteViewSet)
router.register(r"burialgroups", burial_api_views.BurialGroupViewSet)
router.register(r"burials", burial_api_views.BurialViewSet)
router.register(r"urns", burial_api_views.UrnViewSet)
router.register(r"urncovers", burial_api_views.UrnCoverViewSet)
router.register(r"gravegoods", burial_api_views.GraveGoodViewSet)
router.register(r"gravegoodothers", burial_api_views.GraveGoodOtherViewSet)
router.register(r"anthropology", burial_api_views.AnthropologyViewSet)
router.register(r"animalremains", burial_api_views.AnimalRemainsViewSet)
router.register(r"skoslabels", api_views.SkosLabelViewSet)
router.register(r"skosnamespaces", api_views.SkosNamespaceViewSet)
router.register(r"skosconceptschemes", api_views.SkosConceptSchemeViewSet)
router.register(r"skosconcepts", api_views.SkosConceptViewSet)
router.register(r"places", PlaceViewSet)
router.register(r"Book", BookViewSet)


urlpatterns = [
    re_path(r"^api/", include(router.urls)),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^", include("webpage.urls", namespace="webpage")),
    re_path(r"^vocabs/", include("vocabs.urls", namespace="vocabs")),
    re_path(r"^vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    re_path(r"places/", include("places.urls", namespace="places")),
    re_path(r"^bib/", include("bib.urls", namespace="bib")),
    re_path(r"^burials/", include("burials.urls", namespace="burials")),
    re_path(r"^browsing/", include("browsing.urls", namespace="browsing")),
]
