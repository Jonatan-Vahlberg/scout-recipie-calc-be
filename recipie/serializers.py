
from rest_framework import serializers
from .models import Recipie, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'base_amount', 'id', 'unit', 'category')

class RecipieSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipie
        fields = ('name', 'id', 'ingredients', 'link', 'image_link', 'description')