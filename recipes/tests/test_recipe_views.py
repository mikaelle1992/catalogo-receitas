from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views 
from utils.recipes.factory import make_recipe


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view =  resolve(reverse('recipes:home'))
        self.assertIs(view.func.view_class, views.RecipeListViewHome)
    
    def test_recipe_category_view_function_is_correct(self):
        view =  resolve(reverse('recipes:category', kwargs={'category_id':1}))
        self.assertIs(view.func.view_class, views.RecipeListViewCatecory)

    def test_recipe_detail_view_function_is_correct(self):
        view =  resolve(reverse('recipes:recipe', kwargs={'id':1}))
        self.assertIs(view.func.view_class, views.RecipeDetail)
    
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
        response = self.client.get(reverse('recipes:recipe', kwargs={'pk':1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_search_view_function_is_correct(self):
        view =  resolve(reverse('recipes:search'))
        self.assertIs(view.func.view_class, views.RecipeListViewSearch)

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

    # def test_recipe_search_can_find_recipe_by_title(self):
    #      title1 = 'This is recipe one'
    #      title2 = 'This is recipe two'
 
    #      recipe1 = self.make_recipe(
    #          slug='one', title=title1, author_data={'username': 'one'}
    #      )
    #      recipe2 = self.make_recipe(
    #          slug='two', title=title2, author_data={'username': 'two'}
    #      )
 
    #      search_url = reverse('recipes:search')
    #      response1 = self.client.get(f'{search_url}?q={title1}')
    #      response2 = self.client.get(f'{search_url}?q={title2}')
    #      response_both = self.client.get(f'{search_url}?q=this')
 
    #      self.assertIn(recipe1, response1.context['recipes'])
    #      self.assertNotIn(recipe2, response1.context['recipes'])
 
    #      self.assertIn(recipe2, response2.context['recipes'])
    #      self.assertNotIn(recipe1, response2.context['recipes'])
 
    #      self.assertIn(recipe1, response_both.context['recipes'])
    #      self.assertIn(recipe2, response_both.context['recipes'])

    # def test_invalid_page_query_uses_page_one(self):
    #      for i in range(8):
    #          kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
    #          self.make_recipe(**kwargs)
 
    #      with patch('recipes.views.PER_PAGE', new=3):
    #          response = self.client.get(reverse('recipes:home') + '?page=12A')
    #          self.assertEqual(
    #              response.context['recipes'].number,
    #              1
    #          )
    #          response = self.client.get(reverse('recipes:home') + '?page=2')
    #          self.assertEqual(
    #              response.context['recipes'].number,
    #              2
    #          )
    #          response = self.client.get(reverse('recipes:home') + '?page=3')
    #          self.assertEqual(
    #              response.context['recipes'].number,
    #              3
    #          )