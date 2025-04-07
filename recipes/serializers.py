from django.contrib.auth.models import User
from rest_framework import serializers

from authors.validators import AuthorRecipeValidator
from recipes.models import Recipe
from tag.models import Tag
from tag.serializers import TagSerializer

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'category', 'tags', 'public', 'preparation', 'serving','preparation_steps',
            'tag_objects', 'tag_links','servings',  'servings_unit',
            'preparation_time', 'preparation_time_unit','cover'
             
            ]

    public = serializers.BooleanField(source='is_published', read_only= True) #renomeando o nome do campo
    preparation = serializers.SerializerMethodField(read_only=True,)
    serving = serializers.SerializerMethodField(read_only=True,)
    category = serializers.StringRelatedField(read_only=True,)

    tag_objects = TagSerializer(
        many = True, source = 'tags', read_only=True,
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many = True, 
        source = 'tags', 
        # queryset=Tag.objects.all(),
        read_only=True,
        view_name = 'recipes:recipe_tag_api_v2'

    )

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def get_serving(self, recipe):
        return f'{recipe.servings} {recipe.servings_unit}'
    
    def validate(self, attrs):
        if self.instance is not None and attrs.get('servings') is None:
            attrs['servings'] = self.instance.servings
 
        if self.instance is not None and attrs.get('preparation_time') is None:
            attrs['preparation_time'] = self.instance.preparation_time
 
        super_validate = super().validate(attrs)
        AuthorRecipeValidator(data = attrs, ErrorClass=serializers.ValidationError)
        return super_validate
    

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    