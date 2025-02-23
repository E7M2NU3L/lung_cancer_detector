from rest_framework.serializers import ModelSerializer
from lung_classifier.models import CovidModel, LungCancerModel, LungCancerCtModel

class LungCancerSerializer(ModelSerializer):
    class Meta:
        model = LungCancerModel
        fields = "__all__"

class CovidSerializer(ModelSerializer):
    class Meta:
        model = CovidModel
        fields = "__all__"

class LungCancerCTSerializer(ModelSerializer):
    class Meta:
        model = LungCancerCtModel
        fields = "__all__"