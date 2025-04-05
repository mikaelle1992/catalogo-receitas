from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipes.serializers import RecipeSerializer
from recipes.models import Recipe

@api_view()
def recipe_api_list(request):
     recipes = Recipe.objects.get_published()[:10]
     serializer = RecipeSerializer(instance=recipes, many=True)
     return Response(serializer.data)