from django.contrib.auth.models import User
from rest_framework import serializers

from tag.models import Tag
from tag.serializers import TagSerializer

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=165)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published') #renomeando o nome do campo
    preparation = serializers.SerializerMethodField()
    serving = serializers.SerializerMethodField()
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category = serializers.StringRelatedField()
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    tag_objects = TagSerializer(
        many = True, source = 'tags'
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many = True, 
        source = 'tags', 
        queryset=Tag.objects.all(),
        view_name = 'recipes:recipe_tag_api_v2'

    )

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def get_serving(self, recipe):
        return f'{recipe.servings} {recipe.servings_unit}'
    
    
    # preparation_steps = serializers.t
    # preparation_steps_is_html = serializers.BooleanField()
    # created_at = serializers.
    # updated_at = serializers.
    # cover = serializers.
    # category = serializers.
    # on_dele = serializers.
    # 