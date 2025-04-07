from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from recipes.serializers import RecipeSerializer
from recipes.models import Recipe
from tag.models import Tag
from tag.serializers import TagSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

class RecipeApiV2Pagination(PageNumberPagination):
    page_size = 4

class RecipeAPIv2ModelViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeApiV2Pagination

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get('category_id', '')

        if category_id != '' and category_id.isnumeric():
            qs = qs.filter(category_id = category_id)

        return qs


@api_view()
def recipe_api_tag(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(instance=tag, many=False, context={'request':request})
    return Response(serializer.data)
