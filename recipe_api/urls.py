from django.urls import path
from . import views


urlpatterns = [
    path('get-all', views.get_all, name='get-all'),
    path('upload-recipe/', views.upload_recipe, name='upload-recipe')
]

