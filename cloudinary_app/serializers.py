from rest_framework import serializers

class MyImageSerializer(serializers.Serializer):
    url = serializers.CharField()
    public_id = serializers.CharField()
    width = serializers.CharField()
    height = serializers.CharField()
    size = serializers.CharField()
