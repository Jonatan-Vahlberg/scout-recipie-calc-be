from django.db import models
from .enums import IngredientUnit, IngredientCategory, IngredientReplacementReason
# Create your models here.


class Recipie(models.Model):
    ingredients = models.ManyToManyField(
        "Ingredient", through="RecipieIngredient", related_name="recipies")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image_link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=3,
                            choices=IngredientUnit.units,
                            null=True, blank=True
                            )
    category = models.CharField(max_length=20,
                                choices=IngredientCategory.categories,
                                null=True, blank=True
                                )


    def __str__(self):
        return f"{self.name}"
    


class RecipieIngredient(models.Model):
    recipie = models.ForeignKey(Recipie, on_delete=models.CASCADE,)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    replaces = models.IntegerField(null=True, blank=True)
    replaces_reason = models.CharField(
        choices=IngredientReplacementReason.reasons,
        null=True, blank=True, max_length=255
    )
