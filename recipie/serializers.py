
from rest_framework import serializers
from .models import Recipie, Ingredient, RecipieIngredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'id', 'unit', 'category')

class RecipieIngredientSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='ingredient.name')
    unit = serializers.ReadOnlyField(source='ingredient.unit')
    category = serializers.ReadOnlyField(source='ingredient.category')
    ingredient_id = serializers.ReadOnlyField(source='ingredient.id')

    class Meta:
        model = RecipieIngredient
        fields = ('name', 'amount', 'id', 'unit', 'category', 'replaces', 'replaces_reason', 'ingredient_id')

class RecipieSerializer(serializers.ModelSerializer):
    ingredients = RecipieIngredientSerializer(source='recipieingredient_set',many=True, read_only=True)
    class Meta:
        model = Recipie
        fields = ('name', 'id', 'link', 'image_link', 'description', 'ingredients')