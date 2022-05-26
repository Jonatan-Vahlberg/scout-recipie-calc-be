
from rest_framework import serializers
from .models import Recipie, Ingredient, RecipieIngredient

class IngredientListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        items = [Ingredient(**item) for item in validated_data]
        return Ingredient.objects.bulk_create(items, ignore_conflicts=True)

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'id', 'unit', 'category')
        list_serializer_class = IngredientListSerializer

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
    id = serializers.ModelField(model_field=Recipie()._meta.get_field('id'), required=False)

    class Meta:
        model = Recipie
        fields = ('name', 'id', 'link', 'image_link', 'description', 'ingredients')