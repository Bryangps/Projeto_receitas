from django.urls import path
from .views import home, recipe


urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:pk>/', recipe, name='recipe')
]

