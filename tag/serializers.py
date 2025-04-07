from rest_framework import serializers

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=165)
    slug = serializers.SlugField()
