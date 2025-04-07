from django.urls import path
from recipes import views 



app_name ='recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/', views.RecipeListViewCatecory.as_view(), name="category"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),
    path('recipes/tag/<slug:slug>/', views.RecipeListViewTag.as_view(), name="tag"),
    


    path('api/v1/', views.RecipeListViewHomeApi.as_view(), name="home_api"),
    path('api/v1/recipes/<int:pk>/', views.RecipeDetailApi.as_view(), name="recipe_detail_api"),


    # api rest
    path('recipes/api/v2/',views.RecipeAPIv2ModelViewSet.as_view({
        'get':'list',
        'post':'create'
    }), name='recipe_api_list'),
    path('recipes/api/v2/<int:pk>/', views.RecipeAPIv2ModelViewSet.as_view({
        'get':'retrieve',
        'patch':'partial_update',
        'delete':'destroy',
    }), name="recipe_detail_api_v2"),
    path('recipes/api/v2/tag/<int:pk>', views.recipe_api_tag, name="recipe_tag_api_v2"),

]