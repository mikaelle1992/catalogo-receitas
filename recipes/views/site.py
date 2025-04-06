from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.forms.models import model_to_dict
from tag.models import Tag
from utils.pagination import make_pagination
from ..models import Recipe
import os

PER_PAGE = int(os.environ.get('PER_PAGE', 4))



# Create your views here.
class RecipeListViewBase(ListView):
    
    model = Recipe
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = "recipes/pages/home.html"
 

    def get_queryset(self, *args, **kwargs):
        qs =super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True
        )
        qs= qs.select_related('author','category')
        qs = qs.prefetch_related('tags')
        # quando for muitos p/ muitos usar o prefetch_related
        return qs
        
    def get_context_data(self, *args, **kwargs):
        #manipular contexto
        ctx = super().get_context_data(*args, **kwargs)

        page_obj, pagination_range = make_pagination(self.request, ctx.get('recipes'), PER_PAGE)
        ctx.update({
            'recipes':page_obj, 'pagination_range': pagination_range})

        return ctx


class RecipeListViewHome(RecipeListViewBase):
    template_name = "recipes/pages/home.html"

class RecipeListViewHomeApi(RecipeListViewBase):
    template_name = "recipes/pages/home.html"

    def render_to_response(self, context, **response_kwargs):
        recipes = self.get_context_data()['recipes']
        recipes_list = recipes.object_list.values()
 
        return JsonResponse(
            list(recipes_list),
            safe=False
         )

class RecipeListViewCatecory(RecipeListViewBase):
    template_name = "recipes/pages/category.html"

    def get_queryset(self, *args, **kwargs):
        qs =super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            category__id=self.kwargs.get('category_id'),
        )

        if not qs:
             raise Http404()
        
        return qs

class RecipeListViewTag(RecipeListViewBase):
     template_name = 'recipes/pages/tag.html'
 
     def get_queryset(self, *args, **kwargs):
         qs = super().get_queryset(*args, **kwargs)
         qs = qs.filter(tags__slug=self.kwargs.get('slug', ''))
         return qs
 
     def get_context_data(self, *args, **kwargs):
         ctx = super().get_context_data(*args, **kwargs)
         page_title = Tag.objects.filter(
             slug=self.kwargs.get('slug', '')
         ).first()
 
         if not page_title:
             page_title = 'No recipes found'
 
         page_title = f'{page_title} - Tag |'
 
         ctx.update({
             'page_title': page_title,
         })
 
         return ctx
 
 
class RecipeListViewSearch(RecipeListViewBase):
    template_name = 'recipes/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('q','')

        if not search_term:
             raise Http404()
        qs =super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term),
            )
        )[:20]
        # colocar limite no filter '[:10]'
        #ler documentação https://docs.djangoproject.com/pt-br/4.0/ref/models/querysets/#operators-that-return-new-querysets
        return qs 
    

    def get_context_data(self, *args, **kwargs):
        #manipular contexto
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q','')

        ctx.update({
            'page_title':f'Search for "{search_term}"|',
            'search_term': search_term,
            'additional_url_query':f'&q={search_term}'
            })

        return ctx


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/pages/recipe-view.html'

    def get_context_data(self, **kwargs):
        ctx =super().get_context_data(**kwargs)

        ctx.update({
            'is_datail_page':True
            })
        
        return ctx


class RecipeDetailApi(RecipeDetail):
    def render_to_response(self, context, **response_kwargs):
        recipe = self.get_context_data()['recipe']
        recipe_dict = model_to_dict(recipe)
        recipe_dict['created_at'] = str(recipe.created_at)
        recipe_dict['updated_at'] = str(recipe.updated_at)

        if recipe_dict.get('cover'):
            recipe_dict['cover'] = self.request.build_absolute_uri()+ \
                recipe_dict['cover'].url[1:] 
        else:
            recipe_dict['cover'] = ''

        del recipe_dict['is_published']

        return JsonResponse(
            recipe_dict,
            safe=False

        )