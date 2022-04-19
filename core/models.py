from django.db import models
from recipie.models import Recipie
# Create your models here.




class Cart(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    version = models.PositiveIntegerField(default=0)

class CartRecipie(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE,)
    recipie = models.ForeignKey(Recipie, on_delete=models.CASCADE)

class PortionGroup(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    xs = models.PositiveIntegerField(default=0)
    sm = models.PositiveIntegerField(default=0)
    md = models.PositiveIntegerField(default=0)
    lg = models.PositiveIntegerField(default=0)
    xl = models.PositiveIntegerField(default=0)

    VEGITARIAN = models.PositiveIntegerField(default=0)
    VEGAN = models.PositiveIntegerField(default=0)
    DAIRY = models.PositiveIntegerField(default=0)
    MP_ALLERGIES = models.PositiveIntegerField(default=0)
    GLUTEN = models.PositiveIntegerField(default=0)
    LEGUMINOUS = models.PositiveIntegerField(default=0)