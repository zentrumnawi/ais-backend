from rest_framework.serializers import ModelSerializer


class FindSerializer(ModelSerializer):

    class Meta:
        model = None
        fields = "__all__"
        depth = 1

