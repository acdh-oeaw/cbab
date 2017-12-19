from rest_framework import serializers
from .models import *
from vocabs.serializers import *


class BurialSiteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BurialSite
		fields = '__all__'


class BurialGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BurialGroup
        fields = '__all__'


class BurialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Burial
        fields = '__all__'


class UrnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Urn
        fields = '__all__'


class UrnCoverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrnCover
        fields = '__all__'


class GraveGoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GraveGood
        fields = '__all__'


class GraveGoodOtherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GraveGoodOther
        fields = '__all__'


class DeadBodyRemainsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeadBodyRemains
        fields = '__all__'


class AnimalRemainsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimalRemains
        fields = '__all__'