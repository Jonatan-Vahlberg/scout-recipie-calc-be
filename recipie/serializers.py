
from rest_framework import serializers
from .models import Recipie, Ingredient, RecipieIngredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'base_amount', 'id', 'unit', 'category')

class RecipieIngredientSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='ingredient.name')
    unit = serializers.ReadOnlyField(source='ingredient.unit')
    category = serializers.ReadOnlyField(source='ingredient.category')

    class Meta:
        model = RecipieIngredient
        fields = ('name', 'amount', 'id', 'unit', 'category')

class RecipieSerializer(serializers.ModelSerializer):
    ingredients = RecipieIngredientSerializer(source='recipieingredient_set',many=True)
    class Meta:
        model = Recipie
        fields = ('name', 'id', 'ingredients', 'link', 'image_link', 'description')