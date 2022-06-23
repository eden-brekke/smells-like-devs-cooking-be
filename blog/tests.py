from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BlogPost
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class Test_Smells_like_Devs_cCooking(TestCase):
    @classmethod
    
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="Happ33H0ur5"
        )
        testuser1.save()

        test_create_blog = BlogPost.objects.create(
            owner = testuser1,
            recipe_ingredients = "1 can of corn, 1 can of black beans, handful of fresh cilantro, lemon juice, half purple onion diced, 2 diced tomatoes, 4 tbs of chives, salt and pepper to taste",
            recipe_directions = "Strain and rinse corn and black beans, add all ingredients to a bowl mix well., Season as desired., Refrigerate for alteast 30 mins. eat and enjoy!",
            recipe_images = "https://ourzestylife.com/wp-content/uploads/2021/06/Cowboy-Caviar-OurZestyLife-5.jpg",
            title = "SW Corn and Bean Salad",
            difficulty = 2,
            recipe_intro = "Best Summer salad that is also a dip",
            prep_time = 20,
            cook_time = 2,
            meal_type = "Snack",
        )
        test_create_blog.save()
        

    def setUp(self):
      self.client.login(username="testuser1", password="pass")


    def test_blogpost_model(self):
        newRecipe = BlogPost.objects.get(id=1)
        recipe_owner = str(newRecipe.owner)
        recipe_title = str(newRecipe.title)
        recipe_description = str(newRecipe.recipe_intro)
        self.assertEqual(recipe_owner, "testuser1")
        self.assertEqual(recipe_title, "SW Corn and Bean Salad")
        self.assertEqual(recipe_description, "Best Summer salad that is also a dip")

    def test_get_blog_list(self):
          url = reverse("blog_post_list")
          response = self.client.get(url)
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          recipes = response.data
          self.assertEqual(len(recipes), 1)
          self.assertEqual(recipes[0]["title"], "SW Corn and Bean Salad")

    def test_get_recipe_by_id(self):
      url = reverse("blog_post_detail", args=(1,))
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      recipes = response.data
      self.assertEqual(recipes["title"], "SW Corn and Bean Salad")

    # def test_create_recipe(self):
    #   url = reverse("blog_post_list")
    #   data = {"owner": 'testuser1', "name": "Snickers", "recipe_intro": "frozen please"}
    #   response = self.client.post(url, data)
    #   self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #   recipes = BlogPost.objects.all()
    #   self.assertEqual(len(recipes), 2)
    #   self.assertEqual(BlogPost.objects.get(id=2).name, "Snickers")

    # def test_update_recipe(self):
    #     url = reverse("blog_post_detail", args=(1,))
    #     data = {
    #         "owner": 1,
    #         "title": "CornBean Salad",
    #         "recipe_intro": "Summer salad that is also a dip.",
    #     }
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     recipe = BlogPost.objects.get(id=1)
    #     self.assertEqual(recipe.title, data["title"])
    #     self.assertEqual(recipe.owner.id, data["owner"])
    #     self.assertEqual(recipe.recipe_intro, data["recipe_intro"])

    # def test_delete_recipe(self):
    #     url = reverse("blog_post_detail", args=(1,))
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     recipes = BlogPost.objects.all()
    #     self.assertEqual(len(recipes), 0)

    # def test_authentication_required(self):
    #     self.client.logout()
    #     url = reverse("blog_post_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
