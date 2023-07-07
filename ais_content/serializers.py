from solid_backend.utils.serializers import SolidModelSerializer
from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.photograph.serializers import PhotographSerializer

from .models import Find, FormalAspect, Ware, GeneralInformation


class FormalAspectSerializer(SolidModelSerializer):
    class Meta:
        model = FormalAspect
        exclude = ["find"]


class WareSerializer(SolidModelSerializer):
    class Meta:
        model = Ware
        exclude = ["find"]


class GeneralInformationSerializer(SolidModelSerializer):
    class Meta:
        model = GeneralInformation
        exclude = ["find"]


class FindSerializer(SolidModelSerializer):
    general_information = GeneralInformationSerializer()
    formal_aspect = FormalAspectSerializer()
    ware = WareSerializer(required=False)
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Find
        fields = "__all__"
        depth = 1
