from django.urls import path
from .views import home, recipe, category


app_name = 'recipes'


urlpatterns = [
    path('', home, name='home'),
    path('recipes/category/<int:category_id>/', category, name='category'),
    path('recipes/<int:pk>/', recipe, name='recipe')
]

