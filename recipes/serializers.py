from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=165)
    description = serializers.CharField(max_length=165)
    # preparation_time = serializers.IntegerField()
    # preparation_time_unit = serializers.CharField(max_length=65)
    # servings = serializers.IntegerField()
    # servings_unit = serializers.CharField(max_length=65)
    # preparation_steps = serializers.t
    # preparation_steps_is_html = serializers.BooleanField()
    # created_at = serializers.
    # updated_at = serializers.
    # is_published = serializers.
    # cover = serializers.
    # category = serializers.
    # on_dele = serializers.
    # author = serializers.