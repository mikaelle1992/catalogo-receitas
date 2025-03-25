from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')
    return render(request, "recipes/pages/home.html", context={
        'recipes':recipes,
        })


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id).first()
    return render(request, "recipes/pages/recipe-view.html", context={
        'recipe':recipe,
        'is_datail_page':True
        })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        ).order_by('-id')

    if not recipes:
        raise Http404('Not Found.')
    
    return render(request, "recipes/pages/category.html", context={
        'recipes':recipes,
        'title': f'{recipes.first().category.name} - Category'
        })