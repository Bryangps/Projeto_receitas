from django.urls import path
from .views import home, recipe
from django.conf.urls.static import static
from django.conf import settings

app_name = 'recipes'


urlpatterns = [
    path('', home, name='home'),
    path('recipes/<int:pk>/', recipe, name='recipe')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
