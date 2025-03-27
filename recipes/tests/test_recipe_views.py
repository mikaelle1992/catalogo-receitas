from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views 


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
    
    def test_recipe_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')


    def test_recipe_category_view_return_status_code_404_Not_Found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_return_status_code_404_Not_Found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_search_view_function_is_correct(self):
        view =  resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search')+'?q=teste') 
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_return_status_code_404_Not_Found(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_ascaped(self):
        response = self.client.get(reverse('recipes:search')+'?q=teste')
        self.assertIn(
            'Search for &quot;teste&quot;',
            response.content.decode('utf-8')
        )