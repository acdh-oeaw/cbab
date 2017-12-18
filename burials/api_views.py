from rest_framework import viewsets
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.settings import api_settings


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BurialSiteViewSet(viewsets.ModelViewSet):
    queryset = BurialSite.objects.all()
    serializer_class = BurialSiteSerializer


class BurialGroupViewSet(viewsets.ModelViewSet):
    queryset = BurialGroup.objects.all()
    serializer_class = BurialGroupSerializer


class BurialViewSet(viewsets.ModelViewSet):
    queryset = Burial.objects.all()
    serializer_class = BurialSerializer


class UrnViewSet(viewsets.ModelViewSet):
    queryset = Urn.objects.all()
    serializer_class = UrnSerializer


class UrnCoverViewSet(viewsets.ModelViewSet):
    queryset = UrnCover.objects.all()
    serializer_class = UrnCoverSerializer


class GraveGoodViewSet(viewsets.ModelViewSet):
    queryset = GraveGood.objects.all()
    serializer_class = GraveGoodSerializer


class GraveGoodOtherViewSet(viewsets.ModelViewSet):
    queryset = GraveGoodOther.objects.all()
    serializer_class = GraveGoodOtherSerializer


class AnthropologyViewSet(viewsets.ModelViewSet):
    queryset = DeadBodyRemains.objects.all()
    serializer_class = DeadBodyRemainsSerializer


class AnimalRemainsViewSet(viewsets.ModelViewSet):
    queryset = AnimalRemains.objects.all()
    serializer_class = AnimalRemainsSerializer