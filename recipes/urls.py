from django.urls import path
from recipes import views


app_name ='recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name="search"),
    path('recipes/category/<int:category_id>/', views.RecipeListViewCatecory.as_view(), name="category"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"),


    path('api/v1/', views.RecipeListViewHomeApi.as_view(), name="home_api"),
    path('api/v1/recipes/<int:pk>/', views.RecipeDetailApi.as_view(), name="recipe_detail_api"),
    # path('recipes/search/', views.RecipeListViewSearch.as_view(), name="search"),
    # path('recipes/category/<int:category_id>/', views.RecipeListViewCatecory.as_view(), name="category"),

]