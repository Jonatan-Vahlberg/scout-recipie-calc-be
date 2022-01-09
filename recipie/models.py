from django.db import models
from .enums import IngredientUnit, IngredientCategory
# Create your models here.

class Recipie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image_link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    recipie = models.ForeignKey(Recipie, on_delete=models.CASCADE, related_name='ingredients')

    name = models.CharField(max_length=255)
    base_amount = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=3,
        choices=IngredientUnit.units,
        null=True, blank=True
    )
    category=models.CharField(max_length=20,
        choices=IngredientCategory.categories,
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.recipie.name}-{self.name}"
