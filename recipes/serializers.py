from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=165)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published') #renomeando o nome do campo
    preparation = serializers.SerializerMethodField()
    serving = serializers.SerializerMethodField()

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def get_serving(self, recipe):
        return f'{recipe.servings} {recipe.servings_unit}'
    
    # preparation_time = serializers.IntegerField()
    # preparation_time_unit = serializers.CharField(max_length=65)
    # servings = serializers.IntegerField()
    # servings_unit = serializers.CharField(max_length=65)
    # preparation_steps = serializers.t
    # preparation_steps_is_html = serializers.BooleanField()
    # created_at = serializers.
    # updated_at = serializers.
    # cover = serializers.
    # category = serializers.
    # on_dele = serializers.
    # author = serializers.