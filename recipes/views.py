from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
        )
    return render(request, "recipes/pages/home.html", context={'recipes':recipes})


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id).first()
    return render(request, "recipes/pages/recipe-view.html", context={
        'recipe':recipe,
        'is_datail_page':True
        })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        )
    return render(request, "recipes/pages/home.html", context={'recipes':recipes})