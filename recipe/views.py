from django.shortcuts import render
from utils.recipe.factory import make_recipe
from .models import Category, Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html',
                  {'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html',
                  {'recipes': recipes})


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'recipes/pages/recipe-view.html',
                  {'recipe': recipe,
                   'is_detail_page': True})

