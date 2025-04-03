from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View

from authors.forms.recipe_form import AuthorRecipeForm
from recipes.models import Recipe
from authors.forms import LoginForm, RegisterForm
from django.utils.decorators import method_decorator

@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
     name='dispatch'
)
class DashboardRecipe(View):
    def get_id(self, id=None):
        recipe = None

        if id is not None:
            recipe = Recipe.objects.filter(
            is_published=False,
            author=self.request.user,
            id=id
            ).first()

            if not recipe:
                raise Http404()
 
        return recipe
    
    def render_recipe(self, form):

        return render(self.request,'authors/pages/dashboard_recipe.html',
            context={
            'form':form,
        })

    #####################################
    def get(self, request, id=None):
        recipe =self.get_id(id)
        form = AuthorRecipeForm(instance=recipe)
        return self.render_recipe(form)
    
    def post(self, request, id=None):
        recipe =self.get_id(id)

        form = AuthorRecipeForm(
            data= request.POST or None,
            files=request.FILES or None,
            instance=recipe

        )

        if form.is_valid():
            recipe = form.save(commit=False)

            recipe.author = request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False

            recipe.save()

            messages.success(request, 'Your recipes has been saved.')
            return redirect(reverse('authors:dashboard_edit_recipe', args=(recipe.id,)))

        return self.render_recipe(form)
    
    def delete(self, request, id=None):
        ...