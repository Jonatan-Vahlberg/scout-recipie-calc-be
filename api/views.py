from django.shortcuts import render
from rest_framework import generics
from recipie.serializers import RecipieSerializer, IngredientSerializer
from recipie.models import Recipie, Ingredient

# Create your views here.
class RecipieListView(generics.ListCreateAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer
    search_fields= ['name']

    def create(self, request, *args, **kwargs):
        ingredients = request.data.get('ingredients')
        response = super().create(request, *args, **kwargs)
        print(ingredients)
        response_id = response.data.get('id')
        if(response_id is not None):

            def add_recipe(ingredient):
                ingredient['recipie'] = Recipie.objects.get(id=response_id)
                return ingredient
            ingredients = list(map(add_recipe, ingredients))
            for ingredient in ingredients:
                Ingredient.objects.create(**ingredient)
            # Ingredient.objects.bulk_create(ingredients)

            # ingredient_serializer = IngredientSerializer(data=ingredients, many=True)
            # ingredient_serializer.is_valid(raise_exception=True)
            # ingredient_serializer.save()


        return response


class RecipieDetailView(generics.RetrieveAPIView):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializer