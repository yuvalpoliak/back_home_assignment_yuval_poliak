from django.urls import path
from . import views


urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('add-pic/', views.upload_recipe, name='add_pic')
]

