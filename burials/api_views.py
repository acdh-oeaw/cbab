from rest_framework import viewsets
from rest_framework import pagination
from .models import (
    BurialSite,
    BurialGroup,
    Burial,
    Urn,
    UrnCover,
    GraveGood,
    GraveGoodOther,
    DeadBodyRemains,
    AnimalRemains,
)
from .serializers import (
    BurialSiteSerializer,
    BurialGroupSerializer,
    BurialSerializer,
    UrnSerializer,
    UrnCoverSerializer,
    GraveGoodSerializer,
    GraveGoodOtherSerializer,
    DeadBodyRemainsSerializer,
    AnimalRemainsSerializer,
)


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 10000


class BurialSiteViewSet(viewsets.ModelViewSet):
    queryset = BurialSite.objects.all()
    serializer_class = BurialSiteSerializer
    pagination_class = LargeResultsSetPagination


class BurialGroupViewSet(viewsets.ModelViewSet):
    queryset = BurialGroup.objects.all()
    serializer_class = BurialGroupSerializer
    pagination_class = LargeResultsSetPagination


class BurialViewSet(viewsets.ModelViewSet):
    queryset = Burial.objects.all()
    serializer_class = BurialSerializer
    pagination_class = LargeResultsSetPagination


class UrnViewSet(viewsets.ModelViewSet):
    queryset = Urn.objects.all()
    serializer_class = UrnSerializer
    pagination_class = LargeResultsSetPagination


class UrnCoverViewSet(viewsets.ModelViewSet):
    queryset = UrnCover.objects.all()
    serializer_class = UrnCoverSerializer
    pagination_class = LargeResultsSetPagination


class GraveGoodViewSet(viewsets.ModelViewSet):
    queryset = GraveGood.objects.all()
    serializer_class = GraveGoodSerializer
    pagination_class = LargeResultsSetPagination


class GraveGoodOtherViewSet(viewsets.ModelViewSet):
    queryset = GraveGoodOther.objects.all()
    serializer_class = GraveGoodOtherSerializer
    pagination_class = LargeResultsSetPagination


class AnthropologyViewSet(viewsets.ModelViewSet):
    queryset = DeadBodyRemains.objects.all()
    serializer_class = DeadBodyRemainsSerializer
    pagination_class = LargeResultsSetPagination


class AnimalRemainsViewSet(viewsets.ModelViewSet):
    queryset = AnimalRemains.objects.all()
    serializer_class = AnimalRemainsSerializer
    pagination_class = LargeResultsSetPagination
