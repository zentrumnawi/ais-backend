from rest_framework import serializers
from .models import Find, FormalAspect, Ware


class DisplayNameModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] is None, ret.items()))


class FormalAspectSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormalAspect
        exclude = ["find"]
        swagger_schema_fields = {
            "title": str(model._meta.verbose_name)
        }


class WareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ware
        exclude = ["find"]
        swagger_schema_fields = {
            "title": str(model._meta.verbose_name)
        }


class FindSerializer(serializers.ModelSerializer):
    formal_aspect = FormalAspectSerializer()
    ware = WareSerializer()

    class Meta:
        model = Find
        fields = "__all__"
        depth = 1
        swagger_schema_fields = {
            "title": str(model._meta.verbose_name),
        }
