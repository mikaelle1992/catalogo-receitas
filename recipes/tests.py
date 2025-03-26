from django.test import TestCase
from django.urls import reverse, resolve 
from recipes import views 
# Create your tests here.


class RecipeUrlsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEquals(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id':1})
        self.assertEquals(category_url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        recipes_url = reverse('recipes:recipe',kwargs={'id':1})
        self.assertEquals(recipes_url, '/recipes/1/')

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view =  resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    def test_recipe_category_view_function_is_correct(self):
        view =  resolve(reverse('recipes:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view =  resolve(reverse('recipes:recipe', kwargs={'id':1}))
        self.assertIs(view.func, views.recipe)

