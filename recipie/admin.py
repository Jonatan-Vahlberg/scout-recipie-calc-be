from django.contrib import admin
from .models import Recipie, Ingredient

# Register your models here.
admin.site.register(Recipie)
admin.site.register(Ingredient)