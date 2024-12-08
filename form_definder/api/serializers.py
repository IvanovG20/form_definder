from rest_framework import serializers


class FormDataSerializer(serializers.Serializer):
    data = serializers.DictField(child=serializers.CharField())
