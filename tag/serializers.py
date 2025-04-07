from rest_framework import serializers

from tag.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ['id', 'name', 'slug']
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=165)
    # slug = serializers.SlugField()
