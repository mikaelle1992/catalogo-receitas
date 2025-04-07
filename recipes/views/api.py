from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from recipes.serializers import RecipeSerializer
from recipes.models import Recipe
from tag.models import Tag
from tag.serializers import TagSerializer

@api_view()
def recipe_api_list(request):
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(instance=recipes, many=True, context={'request':request})
    return Response(serializer.data)

@api_view()
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.filter(pk=pk).select_related('author','category')
    )
    serializer = RecipeSerializer(instance=recipe, many=False, context={'request':request})
    return Response(serializer.data)


@api_view()
def recipe_api_tag(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(instance=tag, many=False, context={'request':request})
    return Response(serializer.data)
