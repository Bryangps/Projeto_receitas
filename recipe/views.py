from django.shortcuts import render
from utils.recipe.factory import make_recipe
# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html',
                  {'recipes': [make_recipe for _ in range(8)]})


def recipe(request, pk):
    return render(request, 'recipes/pages/recipe-view.html',
                  {'recipe': make_recipe,
                   'is_detail_page': True})

