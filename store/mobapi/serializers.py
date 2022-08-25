from rest_framework import serializers


class BikeSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    colour=serializers.CharField()
    cc=serializers.IntegerField()
    price=serializers.IntegerField()
    brand=serializers.CharField()