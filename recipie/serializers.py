
from operator import itemgetter
from rest_framework import serializers

from recipie.helpers import create_recipie_ingredient, remove_old_recipie_ingredients, update_recipie_ingredient
from .models import Recipie, Ingredient, RecipieIngredient

class IngredientListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        items = [Ingredient(**item) for item in validated_data]
        return Ingredient.objects.bulk_create(items, ignore_conflicts=True)

class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Ingredient()._meta.get_field('id'), required=False)

    class Meta:
        model = Ingredient
        fields = ('name', 'id', 'unit', 'category')
        list_serializer_class = IngredientListSerializer

class RecipieIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False)
    id = serializers.ModelField(model_field=RecipieIngredient()._meta.get_field('id'), required=False)


    class Meta:
        model = RecipieIngredient
        fields = ('amount', 'id', 'replaces', 'replaces_reason', 'ingredient')

class RecipieSerializer(serializers.ModelSerializer):
    ingredients = RecipieIngredientSerializer(source='recipieingredient_set',many=True)
    id = serializers.ModelField(model_field=Recipie()._meta.get_field('id'), required=False)

    class Meta:
        model = Recipie
        fields = ('name', 'id', 'link', 'image_link', 'description', 'ingredients')
        extra_kwargs = {
            'items': {'required': True, 'read_only': False, 'many': True, 'queryset': RecipieIngredient.objects.all()},
        }
    
    def create(self, validated_data):
        ingredients = validated_data.pop('recipieingredient_set',None)
        recipie  = Recipie.objects.create(**validated_data)

        if(ingredients is not None):
            for ingredient in ingredients:
                create_recipie_ingredient(ingredient, recipie)
        return recipie

    def update(self, instance, validated_data):
        ingredients = validated_data.pop('recipieingredient_set', None)
        saved_ingredients = instance.recipieingredient_set.all()
        remove_old_recipie_ingredients(ingredients, saved_ingredients)
        for ingredient in ingredients:
            _item = saved_ingredients.filter(id=ingredient.get('id'),)
            if not _item.exists():
                create_recipie_ingredient(ingredient, instance)
            else:
                update_recipie_ingredient(ingredient, instance)
        instance = super().update(instance, validated_data)
        return instance

