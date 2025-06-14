from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class RecipeUrlsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEquals(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id':1})
        self.assertEquals(category_url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        recipes_url = reverse('recipes:recipe',kwargs={'pk':1})
        self.assertEquals(recipes_url, '/recipes/1/')

    def test_recipe_search_url_is_correct(self):
        recipes_url = reverse('recipes:search')
        self.assertEquals(recipes_url, '/recipes/search/')