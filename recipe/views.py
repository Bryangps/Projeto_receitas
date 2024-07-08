from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html',
                  {'recipes': recipes})


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/category.html',
                  {'recipes': recipes})


def recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk, is_published=True).order_by('-id').first()
    return render(request, 'recipes/pages/recipe-view.html',
                  {'recipe': recipe,
                   'is_detail_page': True})

