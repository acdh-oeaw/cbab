from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from places.apis_views import PlaceViewSet
from bib.api_views import BookViewSet
from burials.api_views import *
from vocabs import api_views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'burialsites', BurialSiteViewSet)
router.register(r'burialgroups', BurialGroupViewSet)
router.register(r'burials', BurialViewSet)
router.register(r'urns', UrnViewSet)
router.register(r'urncovers', UrnCoverViewSet)
router.register(r'gravegoods', GraveGoodViewSet)
router.register(r'gravegoodothers', GraveGoodOtherViewSet)
router.register(r'anthropology', AnthropologyViewSet)
router.register(r'animalremains', AnimalRemainsViewSet)
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'Book', BookViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'places/', include('places.urls', namespace='places')),
    url(r'^bib/', include('bib.urls', namespace='bib')),
    url(r'^burials/', include('burials.urls', namespace='burials')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^api/docs/', include_docs_urls(title='CBAB API', public=False)),
]
