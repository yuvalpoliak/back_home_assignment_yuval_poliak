from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers

import json

from .models import Recipe

# Create your views here.

@api_view(['GET'])
def get_all(request):
    all_recipes = Recipe.objects.all()
    data = serializers.serialize('json', all_recipes)
    print(data)

    return JsonResponse({'data': data})

@api_view(['POST'])
def upload_recipe(req):
    data = json.loads(req.body)
    new_recipe = Recipe(title = data['title'], content = data['content'], vegan = data['vegan'], hot = data['hot'])
    new_recipe.save()
    redirect('/')
    print(new_recipe)
    return Response({'message', 'uploaded'})
