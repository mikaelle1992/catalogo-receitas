from recipes import views 
from rest_framework.routers import SimpleRouter



recipe_api_v2_router = SimpleRouter()
recipe_api_v2_router.register('', views.RecipeAPIv2ModelViewSet, basename='recipes-api')